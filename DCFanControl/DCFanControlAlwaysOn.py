from time import sleep
from gpiozero import LED

fan = LED(4)

while True:
    print('Fan on')
    fan.on()
    sleep(300)
    print('Fan off')
    fan.off()
    sleep(300)
