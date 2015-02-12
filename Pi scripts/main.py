#			Project Air Mail
#		Mississippi State University
#		ECE Senior Design Spring 2015

#  -----------------------
#	Developer: James Tate
#  -----------------------

# This will be a main script that runs when the Raspberry Pi starts
# This script will live in ~/flightcontrol
# to run manual type
# 			~/flightcontrol sudo python main.py
# to run on startup see http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/

# the purpose is to query the flight controller for its current state
# then it will direct the flight controller on which actions to perform


# Idea behind script
# The first action when starting up is to loop until the flight controller
# sends a current state of loiter to the Pi. This means the vehicle has 
# reached its destination and needs directions to either land or return to
# launch a camera will be used to detect a landing location. if one is not 
# detected the vehicle should return to launch.

import time

#this a variable that will be used for testing
i=0


# start up and loop reading state from flight controller, break loop and  
# continue when vehicle is in loiter mode.

# ============================================
# nothing yet just testing press ctl+c to exit
# ============================================
try:
	
	while True:
		print("hello to break out ctl+c")
		time.sleep(2)
except KeyboardInterrupt:
	pass



# start camera system, look for landing for 15 seconds, if landing is 
# detected land and deliver, otherwise return to launch

#			mock opening camera software

i = i + 1
execfile("test.py")




# if landing we need to query flight controller for altitude. when 0
# we are on the ground. we then need to release servos we maight have to
# send a takeoff commend to the flight contoller after delivering

i = i + 1
execfile("test.py")


# after delivering or if no landing we need to return home.




# this is a timer we will use for testing to allow us to view results
n = 5
while (n != 0):
		print ("self distruct in %s") % n
		if n == 1:
			print ("bye")
		time.sleep(1)
		n = n - 1

