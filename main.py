from machine import Pin, ADC
from time import sleep

led = Pin("GP15", Pin.OUT)
# potentiometer = ADC("GP26")
pir_sensor = Pin("GP16", Pin.IN)


while True:
    # voltage = (potentiometer.read_u16() * 3.3) / 65536
    # pir_sensor.value()
    if pir_sensor.value(): # If motion is detected
        led.value(1) # Turn on the LED
    else:
        led.value(0) # Turn off the LED

    sleep(.1)