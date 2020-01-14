from Phidget22.Phidget import *
from Phidget22.Devices.Encoder import *
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

def onPositionChange(self, positionChange, timeChange, indexTriggered):
	print("PositionChange: " + str(positionChange))
	print("TimeChange: " + str(timeChange))
	print("IndexTriggered: " + str(indexTriggered))
	print("----------")

def main():
	#Create your Phidget channels
	encoder0 = Encoder()

	#Set addressing parameters to specify which channel to open (if any)

	#Assign any event handlers you need before calling open so that no events are missed.
	encoder0.setOnPositionChangeHandler(onPositionChange)

	#Open your Phidgets and wait for attachment
	encoder0.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	#Close your Phidgets once the program is done.
	encoder0.close()

main()
