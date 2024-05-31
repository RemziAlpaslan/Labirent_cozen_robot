import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
E1=4
E2=3
GPIO.setup(E1,GPIO.IN)
GPIO.setup(E2,GPIO.IN)
liste1=[]
liste2=[]
count1=0
count2=0

In1,In2 = 27,22
In3,In4 = 23,24

GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)

GPIO.setup(In3,GPIO.OUT)
GPIO.setup(In4,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

while True:
    GPIO.output(In1,GPIO.LOW)
    GPIO.output(In2,GPIO.LOW)
    GPIO.output(In3,GPIO.LOW)
    GPIO.output(In4,GPIO.LOW)
    time.sleep(3)