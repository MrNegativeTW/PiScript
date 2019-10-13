from time import sleep
from gpiozero import LED

print('AutoHeatsink engeged, please keep hands on the wheel.')

# Define GPIO Here
fan = LED(4)

# Change Refresh Rate Here
refresh_rate = 10

print('---Current setting---')
print('Refresh rate: ' + str(refresh_rate))

while True:
    cpu_temp_file = open('/sys/class/thermal/thermal_zone0/temp')
    cpu_temp = int(cpu_temp_file.read())
    cpu_temp_file.close()
    print('CPU temperature: ' + str(cpu_temp) + '\r', end='')

    # Temperature setting, divided by 1000.
    if cpu_temp >= 40000:
        fan.on()
    else:
        fan.off()

    sleep(refresh_rate)
