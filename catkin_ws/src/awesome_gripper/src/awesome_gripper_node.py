#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import Pixel
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor    

class AwesomeGripperNode(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.mh = Adafruit_MotorHAT(addr=0x60)

        self.myMotor = self.mh.getMotor(4)
        # set the speed to start, from 0 (off) to 255 (max speed)
        self.myMotor.setSpeed(150)



        # Setup subscribers
        self.sub_grip = rospy.Subscriber("~gripper_cmd", Pixel, self.gripCmd, queue_size=1)


    def gripCmd(self,msg):
        cmd = msg.u

        if cmd == 0 :
            #print ("STOP")
            rospy.loginfo("ssssssssssssSTOP")
            self.myMotor.run(Adafruit_MotorHAT.RELEASE)
        elif cmd == 1 :
            #print ("OPEN")
            rospy.loginfo("ooooooooooooOPEN")
            self.myMotor.run(Adafruit_MotorHAT.FORWARD)
        elif cmd == 2 :
            #print ("CLOSE")
            rospy.loginfo("ccccccccccccCLOSE")
            self.myMotor.run(Adafruit_MotorHAT.BACKWARD)
        

    def on_shutdown(self):
        #self.driver.setWheelsSpeed(left=0.0,right=0.0)
        rospy.loginfo("[%s] Shutting down."%(rospy.get_name()))
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        del self.mh


if __name__ == '__main__':
    # Initialize the node with rospy
    rospy.init_node('awesome_gripper_node', anonymous=False)
    # Create the DaguCar object
    node = AwesomeGripperNode()
    # Setup proper shutdown behavior 
    rospy.on_shutdown(node.on_shutdown)
    # Keep it spinning to keep the node alive
    rospy.spin()
