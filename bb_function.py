import RPi.GPIO as GPIO
import RPi.GPIO as GPIO2
from time import sleep   #this lets us have a time delay

#set up BCM GPIO numbering
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO2.BCM)

#setup
#Port 22 entry
#Port 27 exit
GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.IN)
count = 0
keepRun = True


def getCount():
    global count
    global keepRun
    try:
        while keepRun:
            if GPIO.input(22) == 0:
                print("Port 22 is broken")
                sleep(0.01)
                if GPIO.input(27) == 0:
                    print("Port 27 is broken")
                    #count += 1
                    addCount(1)
                    sleep(0.7 )
                    keepRun = False
                else:
                    print("Port 27 is unbroken")
                print("Occupancy: ", count)
                
            elif GPIO.input(27) == 0:
                print("Port 27 is broken")
                sleep(0.01)
                if GPIO.input(22) == 0:
                    print("Port 22 is broken")
                    #count -= 1
                    subCount(1)
                    sleep(0.7)# was 6
                    keepRun = False
                else:
                    print("Port 22 is unbroken")
                print("Occupancy: ", count)
            elif GPIO.input(27) == 0 and GPIO.input(22) == 0:
                print("Both")         
            else:
                print("Port 22 is unbroken")
                print("Port 27 is unbroken")
                sleep(0.1) #wait 0.1 seconds
            keepRun = True            
    except KeyboardInterrupt:
        GPIO.cleanup()
        
    
    return count


def addCount(num):
    global count
    count += num
    return count

def subCount(num):
    global count
    count -= num
    return count

getCount()
print(count) 