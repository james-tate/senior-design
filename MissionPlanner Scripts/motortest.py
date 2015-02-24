#			Project Air Mail
#		Mississippi State University
#		ECE Senior Design Spring 2015

#  -----------------------
#	Developer: James Tate
#  -----------------------
#
 
import time

# 	Radio Receiver Channels Table
# | Channel |   Name   | Default Value |
# |---------|----------|---------------|
# |    1    | Roll     |   1500 PWM    |
# |    2    | Pitch    |   1500 PWM    |
# |    3    | Throttle |   RC3_MIN     |
# |    4    | Yaw      |   1500 PWM    |
# |    5    | Mode     |   RC5_MIN     |
# |   6-9   | Not Used |  Min Values   |
# |---------|----------|---------------|

# later we will add functionality to test throttle %
# of liftoff. This will be used to prove one of our
# design constraints.

print 'This script will test the motors'
print 'Starting Motor PWM'

# in order for the flight controller to respond from a reciever input it needs a starting
# pulse width modulation for more on PWM https://learn.sparkfun.com/tutorials/pulse-width-modulation
# this for loop initializes the output channels to an initial pwm
for chan in range (1,5):            # This mimics receiver wiring see table above
	Script.SendRC(chan,1500,True) 	# Script.SendRC(channel, pwm, sendnow) 1500 is the middle position this is needed for 
									# Roll, Pitch, and Yaw

Script.SendRC(3,Script.GetParam('RC3_MIN'),True) # This sets channel 3 "throttle" to the min value ""SO IT DOES NOT FLY AWAY""

time.sleep(5)
# Testing RC functions
# ====================
print 'check motor pwm is working on the radio calibration page'
print 'starting RC test in'
i = 5
for t in range (1,6):
	print "%d" %i
	i = i-1
	time.sleep(1)
	
print ' '
print 'testing roll'
Script.SendRC(1,Script.GetParam('RC1_MAX'),True) 	# Stick to MAX
print 'roll high'
time.sleep(3)
Script.SendRC(1,Script.GetParam('RC1_MIN'),True) 	# Stick to MIN
print 'roll low'
time.sleep(3)
Script.SendRC(1,1500,True)							# Back to Default
print 'roll mid \n'
time.sleep(1)

print 'testing pitch'
Script.SendRC(2,Script.GetParam('RC2_MAX'),True)    # Stick to MAX
print 'pitch high'
time.sleep(3)
Script.SendRC(2,Script.GetParam('RC2_MIN'),True)	# Stick to MIN
print 'pitch low'
time.sleep(3)
Script.SendRC(2,1500,True)							# Back to Default
print 'pitch mid \n'
time.sleep(1)

print 'testing throttle'
Script.SendRC(3,Script.GetParam('RC3_MAX'),True)	# Stick to MAX
print 'throttle high'
time.sleep(3)
Script.SendRC(3,Script.GetParam('RC3_MIN'),True)	# Stick to MIN
print 'throttle low \n'
time.sleep(3)
Script.SendRC(3,1400,True)			# This is to put the throttle in a position so it will accidentally arm when testing yaw
time.sleep(1)

print 'testing yaw'
Script.SendRC(4,Script.GetParam('RC4_MAX'),True)	# Stick to MAX
print 'yaw high'
time.sleep(3)
Script.SendRC(4,Script.GetParam('RC4_MIN'),True)	# Stick to MIN
print 'yaw low'
time.sleep(3)
Script.SendRC(4,1500,True)							# Back to Default
print 'yaw mid \n'
time.sleep(1)

print 'RC TEST DONE!'
# Motor Arming
# ============
# next we will attempt to arm the motors
# the process to arm the motors is here http://copter.ardupilot.com/wiki/flying-arducopter/arming_the_motors/
print 'If PWM worked correctly press the safty switch until it turns red' 
i = 10
for t in range (1,11):
	print '%d' %i
	i = i-1
	time.sleep(1)
print 'trying to arm motors'
Script.SendRC(3,Script.GetParam('RC3_MIN'),False)
Script.SendRC(4,Script.GetParam('RC4_MAX'),True)
Script.WaitFor('ARMING MOTORS', 30000)

# possible need to figure out how to run a thread here to see if it timed out

Script.SendRC(4,1500,True)
print 'Motors are live! WATCH OUT!'

time.sleep(5)

print 'Shutting motors off!'
for chan in range (1,5):            # This mimics receiver wiring see table above
	Script.SendRC(chan,1500,True) 	# Script.SendRC(channel, pwm, sendnow) 1500 is the middle position this is needed for 
									# 		Roll, Pitch, and Yaw

Script.SendRC(3,Script.GetParam('RC3_MIN'),True)  # This sets channel 3 "throttle" to the min value ""SO IT DOES NOT FLY AWAY""
print 'Motors are off! Have a nice Day :)'