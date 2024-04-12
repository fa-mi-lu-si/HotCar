from machine import Pin, ADC
from time import sleep

led_g = Pin("LED", Pin.OUT)

pir_sensor = Pin("GP16", Pin.IN)

fan = Pin("GP2",Pin.OUT)

while True:
    fan.value(not bool(pir_sensor.value()))
    led_g.value(pir_sensor.value())
    
    sleep(2)
