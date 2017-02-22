import unittest
import math
import random
from Pset1 import Control
from Pset1 import GroundVehicle
from Simulator import Simulator

class TestControl(unittest.TestCase):
    def setUp(self):
        random.seed()
        spd = random.uniform(5,10)
        rVel = random.uniform(-math.pi/4,math.pi/4)

        self.c = Control(spd,rVel)

    def tearDown(self):
        pass

    #Constructor
    def testCConSLarge(self):
        try:
            Control(11,random.uniform(-math.pi/4,math.pi/4))
        except ValueError:
            return
        self.fail("testCConSLarge failed")
        

    def testCConSSmall(self):
        try:
            Control(4,random.uniform(-math.pi/4,math.pi/4))
        except ValueError:
            return
        self.fail("testCConSSmall failed")

    def testCConOmegaLarge(self):
        try:
            Control(random.uniform(5,10),math.pi)
        except ValueError:
            return
        self.fail("testCConOmegaLarge failed")
        
    def testCConOmegaSmall(self):
        try:
            Control(random.uniform(5,10),-math.pi)
        except ValueError:
            return
        self.fail("testCConOmegaSmall failed"),

    def testCConSCorrect(self):
        spd = random.uniform(5,10)
        c = Control(spd,random.uniform(-math.pi/4,math.pi/4))
        self.assertEqual(spd,c.getSpeed(),"testSpeedCorrect failed")

    def testCConOmegaCorrect(self):
        omega = random.uniform(-math.pi/4,math.pi/4)
        c = Control(random.uniform(5,10),omega)
        self.assertEqual(omega,c.getRotVel(),"testSpeedCorrect failed")

    #Get Speed and Rotational Velocity
    def testGetSpeed(self):
        spd = random.uniform(5,10)
        c = Control(spd,random.uniform(-math.pi/4,math.pi/4))
        self.assertEqual(spd,c.getSpeed(),"testGetSpeed failed")

    def testGetRotVel(self):
        omega = random.uniform(-math.pi/4,math.pi/4)
        c = Control(random.uniform(5,10),omega)
        self.assertEqual(omega,c.getRotVel(),"testGetRotVel failed")

class TestGroundVehicle(unittest.TestCase):
    def setUp(self):
        random.seed()

        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        spd = random.uniform(5,10)
        rVel = random.uniform(-math.pi/4,math.pi/4)

        self.gv = GroundVehicle([x,y,theta],spd,rVel)

    def tearDown(self):
        pass

    #Constructor
    def testConxLarge(self):
        x = 101
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConxLarge failed")

    def testConxSmall(self):
        x = -1
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConxSmall failed")
        
    def testConyLarge(self):
        x = random.uniform(0,100)
        y = 101
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConyLarge failed")
        
    def testConySmall(self):
        x = random.uniform(0,100)
        y = -1
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConySmall failed")

    def testConThetaLarge(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = math.pi+1
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConThetaLarge failed")
        
    def testConThetaSmall(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = -math.pi-1
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConThetaSmall failed")

    def testConSLarge(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = 11
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConSLarge failed")

    def testConSSmall(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = 4
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConSSmall failed")
        
    def testConOmegaLarge(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = math.pi
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConOmegaLarge failed")

    def testConOmegaSmall(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = -math.pi
        pose = [x,y,theta]

        try:
            GroundVehicle(pose,s,omega)
        except ValueError:
            return
        self.fail("testConOmegaSmall failed")

    def testConxCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)

        self.assertEqual(x,gv.getPosition()[0],"testConyCorrect failed")

    def testConyCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)

        self.assertEqual(y,gv.getPosition()[1],"testConyCorrect failed")

    def testConThetaCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)

        self.assertEqual(theta,gv.getPosition()[2],"testConThetaCorrect failed")

    def testConSCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)
        v = gv.getVelocity()
        st = math.sqrt((v[0])**2+(v[1])**2)

        self.assertAlmostEqual(s,st,2,"testConSCorrect failed")

    def testConOmegaCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)
        v = gv.getVelocity()[2]
        
        self.assertEqual(omega,v,"testConOmegaCorrect failed")
        
    #Get Position and Velocity
    def testGetPosition(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)

        self.assertEqual(pose,gv.getPosition(),"testGetPosition failed")
        
    def testGetVelocity(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)
        s = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)
        pose = [x,y,theta]
        gv = GroundVehicle(pose,s,omega)
        xspd = s*math.cos(theta)
        yspd = s*math.sin(theta)
        vel = [xspd,yspd,omega]

        self.assertEqual(vel,gv.getVelocity(),"testGetVelocity failed")

    #Set Position
    def testSPxLarge(self):
        x = 101
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(100,self.gv.getPosition()[0],"testSPxLarge failed")
        
    def testSPxSmall(self):
        x = -1
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(0,self.gv.getPosition()[0],"testSPxSmall failed")

    def testSPxCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(x,self.gv.getPosition()[0],"testSPxCorrect failed")
        
    def testSPyLarge(self):
        x = random.uniform(0,100)
        y = 101
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(100,self.gv.getPosition()[1],"testSPyLarge failed")

    def testSPySmall(self):
        x = random.uniform(0,100)
        y = -1
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(0,self.gv.getPosition()[1],"testSPySmall failed")

    def testSPyCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(y,self.gv.getPosition()[1],"testSPyCorrect failed")

    def testSPThetaLarge(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = math.pi*3/2

        self.gv.setPosition([x,y,theta])

        self.assertEqual(-math.pi/2,self.gv.getPosition()[2],"testSPThetaLarge failed")

    def testSPThetaSmall(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = -math.pi*3/2

        self.gv.setPosition([x,y,theta])

        self.assertEqual(math.pi/2,self.gv.getPosition()[2],"testSPThetaSmall failed")

    def testSPThetaCorrect(self):
        x = random.uniform(0,100)
        y = random.uniform(0,100)
        theta = random.uniform(-math.pi,math.pi)

        self.gv.setPosition([x,y,theta])

        self.assertEqual(theta,self.gv.getPosition()[2],"testSPThetaCorrect failed")

    #Set Velocity    
    def testSVSLarge(self):
        dotx = 11
        doty = 11
        omega = random.uniform(-math.pi/4,math.pi/4)

        self.gv.setVelocity([dotx,doty,omega])

        self.assertEqual(10,self.gv.spd,"testSVSLarge failed")

    def testSVSSmall(self):
        dotx = 1
        doty = 1
        omega = random.uniform(-math.pi/4,math.pi/4)

        self.gv.setVelocity([dotx,doty,omega])

        self.assertEqual(5,self.gv.spd,"testSVSSmall failed")

    def testSVSCorrect(self):
        spd = 6
        omega = random.uniform(-math.pi/4,math.pi/4)

        self.gv.setVelocity([0,6,omega])

        self.assertEqual(spd,self.gv.spd,"testSVSCorrect failed")
        
    def testSVOmegaLarge(self):
        spd = random.uniform(5,10)
        omega = math.pi

        self.gv.setVelocity([0,spd,omega])

        self.assertEqual(math.pi/4,self.gv.omega,"testSVOmegaLarge failed")

    def testSVOmegaSmall(self):
        spd = random.uniform(5,10)
        omega = -math.pi

        self.gv.setVelocity([0,spd,omega])

        self.assertEqual(-math.pi/4,self.gv.omega,"testSVOmegaSmall failed")

    def testSVOmegaCorrect(self):
        spd = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)

        self.gv.setVelocity([0,spd,omega])

        self.assertEqual(omega,self.gv.omega,"testSVOmegaCorrect failed")

    #Control Vehicle
    def testCVSLarge(self):
        spd = 11
        omega = random.uniform(-math.pi/4,math.pi/4)

        try:
            Control(spd,omega)
        except ValueError:
            return
        self.fail("testCSLarge failed")

    def testCVSSmall(self):
        spd = -1
        omega = random.uniform(-math.pi/4,math.pi/4)

        try:
            Control(spd,omega)
        except ValueError:
            return
        self.fail("testCSSmall failed")

    def testCVSCorrect(self):
        spd = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)

        c = Control(spd,omega)

        self.gv.controlVehicle(c)

        self.assertEqual(spd,self.gv.spd,"testCVSCorrect failed")

    def testCVOmegaLarge(self):
        spd = random.uniform(5,10)
        omega = math.pi

        try:
            Control(spd,omega)
        except ValueError:
            return
        self.fail("testCVOmegaLarge failed")
        
    def testCVOmegaSmall(self):
        spd = random.uniform(5,10)
        omega = -math.pi

        try:
            Control(spd,omega)
        except ValueError:
            return
        self.fail("testCVOmegaSmall failed")
        
    def testCVOmegaCorrect(self):
        spd = random.uniform(5,10)
        omega = random.uniform(-math.pi/4,math.pi/4)

        c = Control(spd,omega)

        self.gv.controlVehicle(c)

        self.assertEqual(omega,self.gv.omega,"testCVOmegaCorrect failed")

    #Update State
    def testUSSecNegative(self):
        s = -1
        ms = 10

        try:
            self.gv.updateState(s,ms)
        except ValueError:
            return
        self.fail("testUSSecNegative failed")

    def testUSMsecNegative(self):
        s = 10
        ms = -1

        try:
            self.gv.updateState(s,ms)
        except ValueError:
            return
        self.fail("testUSMsecNegative failed")

    def testUSCorrect(self):
        s=0
        ms=0
        gv = GroundVehicle([0,0,0],5,0)
        gv.updateState(s,ms)

        self.assertEqual(0,gv.y,"testUSCorrect failed")

class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.s = Simulator()

    def tearDown(self):
        pass

    def testGCS(self):
        self.s.sec = 10

        self.assertEqual(10,self.s.getCurrentSec(),"testGCS failed")

    def testGCMS(self):
        self.s.msec = 10

        self.assertEqual(10,self.s.getCurrentMSec(),"testGCMS failed")

    def testSNSSmall(self):
        self.s.numSides = 5
        self.s.setNumSides(2)

        self.assertEqual(5,self.s.numSides,"testSNSSmall failed")

    def testSNSLarge(self):
        self.s.numSides = 5
        self.s.setNumSides(11)

        self.assertEqual(5,self.s.numSides,"testSNSLarge failed")

    def testSNSCorrect(self):
        self.s.setNumSides(5)

        self.assertEqual(5,self.s.numSides,"testSNSCorrect failed")

    def testGCSecNeg(self):
        s = -1
        ms = 0

        try:
            self.s.getControl(s,ms)
        except ValueError:
            return
        self.fail("testGCSecNeg failed")
        
    def testGCMSecNeg(self):
        s = 0
        ms = -1

        try:
            self.s.getControl(s,ms)
        except ValueError:
            return
        self.fail("testGCSecNeg failed")

    def testGCCorrect(self):
        sec = 0
        msec = 0
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestControl)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGroundVehicle)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimulator)
    unittest.TextTestRunner(verbosity=2).run(suite)
