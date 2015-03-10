from Tkinter import *
import distance
import time


fhome = open('C:\\mission_scripts\\home.txt', 'r+')
homelat = fhome.readline()
homelong = fhome.readline()
fhome.close
homelat = float(homelat)
homelong = float(homelong)

def validate():
	lat = float(elat.get())
	long = float(elong.get())
	alt = float(ealt.get())
	
	km = distance.km2points(lat, long, homelat, homelong)
	miles = distance.km2miles(km)
	if (alt>50):
		takeoff.set("takeoff state: 0")
		Label(master, text="Sorry your altitude should be below 50 meters, currently: " + ealt.get(), fg="white", bg="blue").grid(row=4, 
			column=0, columnspan=2, sticky=W+E)
		ealt.delete(0,END)
	elif (km > 1000000.60934):
		takeoff.set("takeoff state: 0")
		Label(master, text="Sorry the distance has to be under 1 mile, currently: " + str(miles) + " miles away!", 
			fg="white", bg="blue").grid(row=4, column=0, columnspan=2, sticky=W+E, padx=20, pady=20)
		elat.delete(0,END)
		elong.delete(0,END)
	else:
		elat.configure(state='readonly')
		elong.configure(state='readonly')
		ealt.configure(state='readonly')
		takeoff.set("takeoff state: 1")
		Label(master, text="Success you are ready to FLY!\nDestination: %.2f miles\nAltitude: %.0f meters" % (miles,alt), fg="white", bg="blue").grid(row=0, 
			column=2, rowspan=4, padx=20, pady=20, sticky=NS)
		Button(master, text='LAUNCH', command=store, fg="black", bg="green", font="bold").grid(row=0, column=3, 
			rowspan=2, sticky=N+S+E+W, ipadx=10, ipady=10, padx=10, pady=10)
		Button(master, text='ABORT', command=master.quit, fg="black", bg="red").grid(row=2, column=3, 
			rowspan=2, sticky=N+S+E+W, ipadx=10, ipady=5, padx=10, pady=10)
		
def store():
	if ("takeoff state: 1" == etakeoff.get()):
		print "Writing Delivery Location to File "
		f = open('C:\\mission_scripts\\coords.txt', 'w')
		latout = elat.get()
		longout = elong.get()
		altout = ealt.get()
		f.write(latout)
		f.write('\n')
		f.write(longout)
		f.write('\n')
		f.write(altout)
		f.close()
		time.sleep(3)
		master.quit()
	else:
		Label(master, text="Sorry you need a takeoff code of 1", fg="white", bg="blue").grid(row=0, 
			column=2, rowspan=4, padx=20, pady=20, sticky=NS)
		


master = Tk()
#Lables to let the user know what values to enter
Label(master, text="Latitude (decimal format xx.xxx)").grid(row=0)
Label(master, text="Longitude (decimal format xx.xxx)").grid(row=1)
Label(master, text="Altitude").grid(row=2)

#Entry boxes for values
elat = Entry(master)
elong = Entry(master)
ealt = Entry(master)

#default values and entry size
elat.insert(10,"1")
elong.insert(10,"1")
ealt.insert(10,"15")
takeoff = StringVar()
takeoff.set("takeoff state: 0")
etakeoff = Entry(master, textvariable=takeoff)
etakeoff.configure(state='readonly')

#set focus to latitude
elat.focus_set()

elat.grid(row=0, column=1)
elong.grid(row=1, column=1)
ealt.grid(row=2, column=1)
etakeoff.grid(row=3, column=0)

#Button(master, text='Quit', command=master.quit).grid(row=0, column=3, sticky=W+E)
Button(master, text='Validate', command=validate).grid(row=3, column=1, sticky=W+E, pady=4, padx=4)
master.title("Air Mail")
mainloop( )