import sys
from robot.UR3eRobotInitialisation import robot3, robot4



def testMain():

    posRobot3 = robot3.getActualTCPPose()
    posRobot3[0] = posRobot3[0] -0.01
    posRobot3[1] = posRobot3[1] -0.01
    posRobot3[2] = posRobot3[2] -0.01
    posRobot3[3] = posRobot3[3] -0.01
    posRobot3[4] = posRobot3[4] -0.01
    posRobot3[5] = posRobot3[5] -0.01
    robot3.moveL(posRobot3)
    
    posRobot4 = robot3Receive.getActualTCPPose()
    posRobot4[0] = posRobot4[0] -0.01
    posRobot4[1] = posRobot4[1] -0.01
    posRobot4[2] = posRobot4[2] -0.01
    posRobot4[3] = posRobot4[3] -0.01
    posRobot4[4] = posRobot4[4] -0.01
    posRobot4[5] = posRobot4[5] -0.01
    robot4.moveL(posRobot4)
    
    
    

############################################################################################
#   STARTE PROGRAMM
############################################################################################
if __name__ == "__main__":
    testMain()