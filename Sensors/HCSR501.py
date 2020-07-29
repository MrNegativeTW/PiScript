import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

MONITOR_PIN = 14

GPIO.setup(MONITOR_PIN, GPIO.IN)

try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        print(GPIO.input(MONITOR_PIN))
        time.sleep(0.5)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()