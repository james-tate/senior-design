import math

Eradius = 6378137

def km2points(lata, longa, latb, longb):
	
	diffLat = math.radians(latb- lata)
	diffLong = math.radians(longb - longa)
	#calculates great circle distance using formulas from http://en.wikipedia.org/wiki/Great-circle_distance
	x = (math.sin(diffLat / 2) * math.sin(diffLat / 2)) + (math.cos(math.radians(lata)) * math.cos(math.radians(latb)) * math.sin(diffLong / 2) * math.sin(diffLong / 2))
	
	y = 2 * math.atan2(math.sqrt(x), math.sqrt(1 - x))
	z = Eradius * y
	z = z / 1000
	
	return z

def km2miles(km):
	return km * .621371