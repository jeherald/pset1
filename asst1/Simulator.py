import math
import random
import numpy as np
from Pset1 import Control
from Pset1 import GroundVehicle

# The way I was going to try to impliment this was as follows:
# -Find the the coirdinates of the corners of the shape that are
#   Circumscribed on the circle
# -Find the center of the turns at each of the corner and their
#   radius
# -FInd the Coordinates where the vehichle would have to begin
#   and finish turning
# -Set a speed and rotational velocity such that in n 10 mili-
#   second timesteps, the vehicle would have moved the exact
#   distance from the start and stop turn points (vise versa
#   if the vehicle was ona straight away)
# -Impliment getControl() so that when the vehicle is on a
#   start or stop turn point, the rotational velocity and
#   speed will be updated
# -Impliment run and main as discribed in the directions
#
# I ran into a couple issues trying to find the proper speed
#   and stop and start turn points. I feel like I was on the
#   right path, I was just unable to finish due to mathmatical
#   errors

class Simulator:
    def __init__(self):
        self.sec = 0
        self.msec = 0
        self.numSides = 5
        
        thetastart = math.pi/2
        self.degAtCorner = math.pi-self.interiorAngle(self.numSides)
        self.turnTime = 3.5
        self.straightTime = 5.5
        self.RotVel = self.degAtCorner/self.turnTime
        self.radiusOfCorner = 5
        
        self.corners=0
        self.setCorners(self.numSides)
        self.turnCenters=0
        self.turnStarts=0
        self.turnStops=0
        self.setTurnCenters(self.numSides)
        self.strDist = math.sqrt((self.turnStarts[0][0]-self.turnStops[0][0])**2+(self.turnStarts[0][1]-self.turnStops[0][1])**2)
        self.spd = 5#self.strDist/self.straightTime
        
        gv = GroundVehicle([0,0,thetastart],self.spd,self.RotVel)
        self.clock = self.sec+self.msec*0.001

    def getCurrentSec(self):
        return self.sec

    def getCurrentMSec(self):
        return self.msec

    def setCorners(self,num):
        self.corners = np.zeros((num,2))
        self.corners[0] = [0.0,25.0]
        difangle = math.pi*2/num
        
        for i in range(1,num):
            anglefromzero=i*difangle
            x = 25*math.cos(90.0-anglefromzero)
            y = 25*math.sin(90.0-anglefromzero)
            self.corners[i] = [x,y]
        
    def setTurnCenters(self,num):
        self.corners = np.zeros((num,2))
        self.turnStarts = np.zeros((num,2))
        self.turnStops = np.zeros((num,2))
        difangle = math.pi*2/num
        
        for i in range(0,num):
            anglefromzero=90.0-i*difangle
            x = (25-self.radiusOfCorner)*math.cos(anglefromzero)
            y = (25-self.radiusOfCorner)*math.sin(anglefromzero)
            self.corners[i] = [x,y]
            xsrt = x + self.radiusOfCorner*math.cos(anglefromzero-.5*self.degAtCorner)
            ysrt = y + self.radiusOfCorner*math.sin(anglefromzero-.5*self.degAtCorner)
            self.turnStarts[i] = [xsrt,ysrt]

            xstp = x + self.radiusOfCorner*math.cos(anglefromzero+.5*self.degAtCorner)
            ystp = y + self.radiusOfCorner*math.sin(anglefromzero+.5*self.degAtCorner)
            self.turnStops[i] = [xstp,ystp]

    def getControl(self,sec,msec):
        if sec < 0 or msec < 0:
            raise ValueError("Seconds and miliseconds must be grater than 0")
        return
    def interiorAngle(self,num):
        return (num-2)*math.pi/num

    def setNumSides(self,n):
        if n > 10 or n < 3:
            self.numSides=self.numSides
        else:
            self.numSides = n

    def run():
        while self.clock < 100.0:
            c = getControl(self.sec,self.msec)
            gv.controlVehicle(c)
            gv.updateState(self.sec,self.msec)
            #print (self.clock gv.getPosition)

            self.clock+=10.0
            self.sec=int(self.clock)
            self.msec=(self.clock-self.sec)*1000
