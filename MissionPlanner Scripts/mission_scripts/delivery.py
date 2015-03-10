#this will be the main script that runs in Mission Planner
print 'Loading Please Wait'

import sys
import time
import os
import os.path
import subprocess
import MissionPlanner #import *
import clr
clr.AddReference("MissionPlanner.Utilities")

path = r"C:\\Program Files (x86)\\coords.py"
path = 'cmd /c start ' + path
i = 1
fhome = open('C:\\mission_scripts\\home.txt', 'w')
fhome.write(str(cs.lat))
fhome.write('\n')
fhome.write(str(cs.lng))
fhome.close()
time.sleep(1) #allow for write

subprocess.Popen('cmd /c start C:\\mission_scripts\\gui.py')

print 'Waiting for Waypoints'
while os.path.isfile('C:\\mission_scripts\\coords.txt')  == 0:
	print 'Waiting for GPS coordinates'
	time.sleep(3)
print 'Reading GPS coordinates'

f = open('C:\\mission_scripts\\coords.txt', 'r+')
latin = f.readline()
longin = f.readline()
altin = f.readline()
f.close()
lat = float(str(latin)) 
print 'lat is:', lat
long = float(str(longin)) 
print 'long is:', long
alt = float(str(altin))
print 'alt is:', alt 

print 'preparing to start mission'
Script.ChangeMode('Guided')
wp = MissionPlanner.Utilities.Locationwp() # creating waypoint
MissionPlanner.Utilities.Locationwp.lat.SetValue(wp,lat)     # sets latitude
MissionPlanner.Utilities.Locationwp.lng.SetValue(wp,long)   # sets longitude
MissionPlanner.Utilities.Locationwp.alt.SetValue(wp,alt)     # sets altitude
print 'Starting Mission' 
MAV.setGuidedModeWP(wp)

while cs.lat != lat:
	print 'Moving to Latitude'
	time.sleep(3)
while cs.lng != long:
	print 'Moving to Longitude'
	time.sleep(3)

print 'hovering over target'
Script.ChangeMode("Loiter")
	 

time.sleep(1)

time.sleep(3)
os.remove('C:/mission_scripts/coords.txt')
os.remove('C:/mission_scripts/home.txt')

time.sleep(5)

print 'Mission Finished'