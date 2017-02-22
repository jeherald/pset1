import math

class Control:
    def __init__(self, s, omega):
        if s < 5 or s > 10:
            raise ValueError("Speed must be between 5 and 10")
        if omega < - math.pi/4 or omega > math.pi/4:
            raise ValueError("Omega must be between -pi/4 and pi/4")
        self.spd = s
        self.rVel = omega
    def getSpeed(self):
        return self.spd
    def getRotVel(self):
        return self.rVel
    
    @staticmethod
    def inBounds(upperB, lowerB, num):
        if num >= upperB:
            return upperB
        if num <= lowerB:
            return lowerB
        return num

class GroundVehicle:
    def __init__(self,pose,s,omega):
        if pose[0] < 0 or pose[0] > 100:
            raise ValueError("X must be between 0 and 100")
        if pose[1] < 0 or pose[1] > 100:
            raise ValueError("Y must be between 0 and 100")
        if pose[2] < -math.pi or pose[2] > math.pi:
            raise ValueError("Theta must be between -pi and pi")
        if s < 5 or s > 10:
            raise ValueError("Speed must be between 5 and 10")
        if omega < - math.pi/4 or omega > math.pi/4:
            raise ValueError("Omega must be between -pi/4 and pi/4")
        self.x = pose[0]
        self.y = pose[1]
        self.theta = pose[2];
        self.spd = s
        self.rVel = omega

    def getPosition(self):
        return [self.x,self.y,self.theta]
    
    def getVelocity(self):
        return [math.cos(self.theta)*self.spd,math.sin(self.theta)*self.spd,self.rVel]
    
    def setPosition(self,pose):
        self.x = GroundVehicle.inBounds(100,0,pose[0])
        self.y = GroundVehicle.inBounds(100,0,pose[1])
        if pose[2]<0:
            self.theta = pose[2]%(-2*math.pi);
        else:
            self.theta = pose[2]%(2*math.pi);
        if self.theta > math.pi:
            self.theta-=2*math.pi
        elif self.theta < -math.pi:
            self.theta+=2*math.pi
        
    def setVelocity(self,vel):
        self.spd = GroundVehicle.inBounds(10,5,math.sqrt(vel[0]**2+vel[1]**2))
        self.omega = GroundVehicle.inBounds(math.pi/4,-math.pi/4,vel[2])
        
    def controlVehicle(self,c):
        self.spd = GroundVehicle.inBounds(10,5,c.getSpeed())
        self.omega = GroundVehicle.inBounds(math.pi/4,-math.pi/4,c.getRotVel())
        
    def updateState(self,sec,msec):
        if sec <0 or msec < 0:
            raise ValueError("Seconds and miliseconds must be grater than 0")
        t = sec + msec/1000.0

        if self.rVel == 0:
            dx = math.cos(self.theta)*self.spd
            dy = math.sin(self.theta)*self.spd
        else:
            dx = self.spd/self.rVel*(math.sin(self.theta + self.rVel*t) - math.sin(self.theta))
            dy = -self.spd/self.rVel*(math.cos(self.theta + self.rVel*t) - math.cos(self.theta))

        self.x += dx*t
        self.y += dy*t
        self.theta += self.rVel*t
        self.x = GroundVehicle.inBounds(100,0,self.x)
        self.y = GroundVehicle.inBounds(100,0,self.y)
        self.theta = self.theta%(2*math.pi);
        if self.theta > math.pi:
            self.theta-=2*math.pi
        elif self.theta < -math.pi:
            selt.theta+=2*math.pi
    
    @staticmethod
    def inBounds(upperB, lowerB, num):
        if num >= upperB:
            return upperB
        if num <= lowerB:
            return lowerB
        return num
