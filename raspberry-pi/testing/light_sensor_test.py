import time

import RPi.GPIO as GPIO

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up pin 17 for input
SENSOR_PIN = 17
GPIO.setup(SENSOR_PIN, GPIO.IN)


def read_sensor():
    return GPIO.input(SENSOR_PIN)


try:
    while True:
        sensor_value = read_sensor()
        print("Sensor Value:", sensor_value)
        time.sleep(1)  # Wait for 1 second before reading the sensor again

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()  # Clean up the GPIO to reset the pin modes
