import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 14
GPIO_ECHO = 15

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
    
try:  
    print("測量中")

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    # Allow module to settle
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
      start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
      stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000

    # That was the distance there and back so halve the value
    distance = distance / 2

    print("距離 : %.1f" % distance)
    
    time.sleep(1.0)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()