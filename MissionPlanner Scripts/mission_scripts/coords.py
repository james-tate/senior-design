#this script will handle the gps coordinates entry.

import time
import distance
from decimal import *

#this will be replaced later with cs.lat and cs.lng will need to do this from delivery.py and pass them in a file
print 'enter home coords'
print 'simrall coords = 33.452, -88.787'
homelat = 33.452# input('home lat ')
homelong = -88.787# input('home long ')

good = False
while good == False:
	alt = input('enter flying alt ')
	if (alt > 50):
		print 'sorry the alt is too high'
	else:
		good = True

good = False

while good == False:
	lat = input('enter lat ')
	long = input('enter long ')
	print 'verifying coordinates are not out of range'
	print '\n'
	km = distance.km2points(lat, long, homelat, homelong)
	miles = distance.km2miles(km)
	if (km > 1.60934):
		print 'sorry the entered coordinates are out of range'
		print 'the distance is %.2f miles' % miles
	else:
		print 'delivery distance: %.2f km - %.2f miles' % (km, miles)
		good = True
		


time.sleep(1)
print 'writing coords to file'

f = open('C:\\mission_scripts\\coords.txt', 'w')

latout = str(lat)
longout = str(long)
altout = str(alt)

f.write(latout)
f.write('\n')
f.write(longout)
f.write('\n')
f.write(altout)
f.close()
time.sleep(3)