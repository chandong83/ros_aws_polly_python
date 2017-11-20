# ros_aws_polly_python
aws(amazon web service) polly by python


amazon polly TTS for ROS


It currently supports Only Korean('eoyeon') and English('Joanna').
The language is automatically detected.

## requirement  

You must have credentials access key of aws first.<br>
please refer to the link below.<br>
http://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/id_credentials_access-keys.html

<pre><code>
#Python Packages

$ pip install boto3 # Amazon SDK
$ pip install python-vlc   # vlc player
</code>
</pre>


## Code Download and Build  
<pre><code>
$ cd catkin_ws/src  # move to your src of catkin workspace
$ git clone https://github.com/chandong83/ros_aws_polly_python   # Download source code
$ cd ..  # move to your catkin workspace
$ catkin_make   # build

# after build success
$ . devel/setup.bash
</code>
</pre>


## Run ROS and Test
<pre><code>
# start roscore with daemon
$ roscore &

# start amazon polly service
$ rosrun amazon_polly aws_polly_tts

# test TTS
$ rosrun amazon_polly hello 
</code>
</pre>


## youtube link
https://youtu.be/FUPQo6w7LHY


## blog
http://blog.naver.com/chandong83/221143018147


