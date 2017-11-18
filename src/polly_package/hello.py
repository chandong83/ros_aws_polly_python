#! /usr/bin/env python
# -*- coding: utf-8 -*-
import polly_package.hello

def say (name) :
    talker(name)

#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker(text):
    pub = rospy.Publisher('aws_tts', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #text = "안녕하세요. 저는 아스리에요." #"hello my name is asule" # %s" % rospy.get_time()
    rospy.loginfo(text)
    pub.publish(text)
    rate.sleep()

if __name__ == '__main__':
    try:
        talker("안녕하세요. 저는 아스리에요.")
    except rospy.ROSInterruptException:
        pass
