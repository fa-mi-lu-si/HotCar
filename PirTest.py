from machine import Pin, ADC
from time import sleep

led_g = Pin("LED", Pin.OUT)
pir_sensor = Pin("GP16", Pin.IN)

while True:

    if pir_sensor.value():  # If motion is detected
        led_g.value(1)  # Turn on the LED
    else:
        led_g.value(0)  # Turn off the LED

    sleep(0.1)
