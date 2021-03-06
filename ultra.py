import matplotlib.pyplot as plt
import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

TRIG = 20                                  #Associate pin 23 to TRIG
ECHO = 21                                  #Associate pin 24 to ECHO


GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

def get_distance():
  pulse_end = 1
  pulse_start = 2
  GPIO.output(TRIG, False)  # Set TRIG as LOW
  time.sleep(0.1)
  GPIO.output(TRIG, True)  # Set TRIG as HIGH
  time.sleep(0.00001)  # Delay of 0.00001 seconds
  GPIO.output(TRIG, False)
  while GPIO.input(ECHO) == 0:  # Check whether the ECHO is LOW
    pulse_start = time.time()  # Saves the last known time of LOW pulse

  while GPIO.input(ECHO) == 1:  # Check whether the ECHO is HIGH
    pulse_end = time.time()  # Saves the last known time of HIGH pulse

  pulse_duration = pulse_end - pulse_start  # Get pulse duration to a variable

  distance = pulse_duration * 17150  # Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)
  return distance


def example():
  D = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

  while True:

    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(0.1)                            #Delay of 2 seconds

    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                      #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW

    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
      pulse_start = time.time()              #Saves the last known time of LOW pulse

    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
      pulse_end = time.time()                #Saves the last known time of HIGH pulse

    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
    distance = round(distance, 2)            #Round to two decimal points

    if distance > 2 and distance < 400:      #Check whether the distance is within range
      print "Distance:",distance ,"cm"  #Print distance with 0.5 cm calibration
    else:
      print "Out Of Range"                   #display out of range

    D.pop(0)
    D.append(distance)
    plt.cla()
    plt.plot(D)
    plt.pause(0.000000000001)

print(get_distance())
