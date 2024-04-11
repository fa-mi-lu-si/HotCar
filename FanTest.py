from machine import Pin
from time import sleep

fan = Pin("GP2",Pin.OUT)

while True:
    fan.toggle()
    sleep(5)
