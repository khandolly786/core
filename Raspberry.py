import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Blink the LED connected to pin 18
try:
    while True:
        GPIO.output(18, GPIO.HIGH)  # Turn on LED
        time.sleep(1)  # Wait for 1 second
        GPIO.output(18, GPIO.LOW)   # Turn off LED
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up the GPIO pins when interrupted
