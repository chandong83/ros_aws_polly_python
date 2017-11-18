#!/usr/bin/env python
# -*- coding: utf-8 -*-
# for ros
import rospy
from std_msgs.msg import String


# for amazon
import re
import os
import sys
from boto3 import client
from botocore.exceptions import BotoCoreError, ClientError
import vlc

ttsQueue = []
languageModel = ["Seoyeon", "Joanna"]

KOREAN = 0
ENGLISH = 1

def isHangul(text):
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0

def ttsProc():
    #if ttsQueue is Empty, return
    if(len(ttsQueue) == 0):
        return

    # bring one Text
    text = ttsQueue.pop()

    # check Hangul
    if isHangul(text):
        # Korean
        voiceid = languageModel[KOREAN]
    else:
        # English
        voiceid = languageModel[ENGLISH]

    try:
        polly = client("polly", region_name="ap-northeast-2")

        response = polly.synthesize_speech(
                Text=text,
                OutputFormat="mp3",
                VoiceId=voiceid)

        #print(response)

        # get Audio Stream (mp3 format)
        stream = response.get("AudioStream")

        # save the audio Stream File
        with open('aws_test_tts.mp3', 'wb') as f:
            data = stream.read()
            f.write(data)

        #play audio file by VLC
        p = vlc.MediaPlayer('aws_test_tts.mp3')
        p.play()

    except ( BotoCoreError, ClientError) as err:
        print(str(err))


def requestCallback(data):
    ttsQueue.append(data.data)


def aws_polly():
    rospy.init_node('aws_polly', anonymous=True)
    rospy.Subscriber("aws_tts", String, requestCallback)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        ttsProc()
        rate.sleep()

if __name__ == '__main__':
    aws_polly()
