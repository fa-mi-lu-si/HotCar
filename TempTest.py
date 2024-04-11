from machine import Pin, ADC
from time import sleep
# from DHT11 import DHT11
import dht

temp_sensor = dht.DHT11(Pin("GP0"))

while True:
    try:
        temp_sensor.measure()
        print(f"Temperature is {temp_sensor.temperature()}")
    except OSError as e:
        print('Failed to read sensor.')

    sleep(1.5)