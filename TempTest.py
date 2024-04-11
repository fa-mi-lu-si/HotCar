from machine import Pin, I2C
from time import sleep
import dht

temp_sensor = dht.DHT22(Pin("GP0"))

while True:
    try:
        temp_sensor.measure()
        print(f"Temperature : {temp_sensor.temperature()}")
        print(f"Humidity : {temp_sensor.humidity()}")
    except OSError as e:
        print('Failed to read sensor.')
    sleep(5)
