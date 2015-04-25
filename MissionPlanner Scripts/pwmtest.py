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
time.sleep(10)
print 'this script will test Receiver PWM functionality'
print 'first we ensure channels 1,2,4 are 1500 PWM'
print 'and throttle is at a value of RC3_MIN (minimum value)'
time.sleep(6)

for chan in range (1,5):            # This mimics receiver wiring see table above
	Script.SendRC(chan,1500,True) 	# Script.SendRC(channel, pwm, sendnow) 1500 is the middle position this is needed for 
									# Roll, Pitch, and Yaw

Script.SendRC(3,Script.GetParam('RC3_MIN'),True) # This sets channel 3 "throttle" to the min value ""SO IT DOES NOT FLY AWAY""

print 'next we begin the test \n'

print 'testing roll'
Script.SendRC(1,Script.GetParam('RC1_MAX'),True) 	# Stick to MAX
print 'roll high'
time.sleep(3)
Script.SendRC(1,Script.GetParam('RC1_MIN'),True) 	# Stick to MIN
print 'roll low'
time.sleep(3)
Script.SendRC(1,1500,True)							# Back to Default
print 'roll mid \n'
time.sleep(4)

print 'testing pitch'
Script.SendRC(2,Script.GetParam('RC2_MAX'),True)    # Stick to MAX
print 'pitch high'
time.sleep(3)
Script.SendRC(2,Script.GetParam('RC2_MIN'),True)	# Stick to MIN
print 'pitch low'
time.sleep(3)
Script.SendRC(2,1500,True)							# Back to Default
print 'pitch mid \n'
time.sleep(4)

print 'testing throttle'
Script.SendRC(3,Script.GetParam('RC3_MAX'),True)	# Stick to MAX
print 'throttle high'
time.sleep(3)
Script.SendRC(3,Script.GetParam('RC3_MIN'),True)	# Stick to MIN
print 'we need to put the throttle in a position so it will not arm and fly away!\n'
time.sleep(3)
Script.SendRC(3,1400,True)			# This is to put the throttle in a position so it will accidentally arm when testing yaw
time.sleep(4)

print 'testing yaw'
Script.SendRC(4,Script.GetParam('RC4_MAX'),True)	# Stick to MAX
print 'yaw high'
time.sleep(3)
Script.SendRC(4,Script.GetParam('RC4_MIN'),True)	# Stick to MIN
print 'yaw low'
time.sleep(3)
Script.SendRC(4,1500,True)							# Back to Default
print 'yaw mid \n'
time.sleep(4)

print 'RC TEST DONE!'
print 'Putting default values back'
for chan in range (1,5):            # This mimics receiver wiring see table above
	Script.SendRC(chan,1500,True) 	# Script.SendRC(channel, pwm, sendnow) 1500 is the middle position this is needed for 
									# 		Roll, Pitch, and Yaw

Script.SendRC(3,Script.GetParam('RC3_MIN'),True)  # This sets channel 3 "throttle" to the min value ""SO IT DOES NOT FLY AWAY""
print 'Motors are off! Have a nice Day :)'