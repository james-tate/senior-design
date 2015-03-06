#this script will handle the gps coordinates entry.

import time

lat = input('enter lat ')
long = input('enter long ')
alt = input('enter alt ')
print 'lat is:', lat
print 'long is:', long
print 'alt is:', alt
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
time.sleep(2)