#this will be the main script that runs in Mission Planner

import time
import os
import os.path
import subprocess

path = r"C:\\Program Files (x86)\\coords.py"
path = 'cmd /c start ' + path
i = 1
time.sleep(1)
subprocess.Popen('cmd /c start C:\\mission_scripts\\coords.py')

print 'reading waypoint from file'
while os.path.isfile('C:\\mission_scripts\\coords.txt')  == 0:
	print 'Waiting for GPS coordinates'
	time.sleep(3)
	
print 'Reading GPS coordinates'

f = open('C:\\mission_scripts\\coords.txt', 'r+')
latin = f.readline()
longin = f.readline()
altin = f.readline()
lat = float(str(latin)) 
print 'lat is:', lat
long = float(str(longin)) 
print 'long is:', long
alt = float(str(altin))
print 'alt is:', alt 

time.sleep(1)


f.close()
time.sleep(3)
os.remove('C:/mission_scripts/coords.txt')\

print 'Starting Mission'

time.sleep(5)

print 'Mission Finished'