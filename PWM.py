import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

trig = 3
echo = 5
led = 7
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

pwm = GPIO.PWM(led,100)
pwm.start(0);

def pwd():
    GPIO.output(trig, True)
    time.sleep(0.01)
    GPIO.output(trig,False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(echo) == 0:
        start = time.time()
        
    while GPIO.input(echo) == 1:
        stop = time.time()
        
    elapsedTime = stop - start
    distance  = (elapsedTime * 34300)/2
    
    if(distance<=60):
        print(distance , "distance")
        pwm.ChangeDutyCycle(100 - distance)
        time.sleep(0.5)
        
    elif(distance > 60): # to prevent code from crashing
        print("No object detected")
        distance = 60
        pwm.ChangeDutyCycle(0)
        time.sleep(0.01)
        
try:
    while True:
        pwd()
               
except KeyboardInterrupt:
    GPIO.cleanup()
    

