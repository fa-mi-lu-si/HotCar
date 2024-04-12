import utime
from machine import Pin, PWM

servo_pin = Pin("GP3", Pin.OUT)
servo = PWM(servo_pin)

# Set the PWM frequency to 50Hz (standard for servos)
servo.freq(50)

# Define the servo positions in microseconds
min_pos = 1000
max_pos = 2000
mid_pos = (min_pos + max_pos) / 2

def angle_to_us(angle):
    return int(min_pos + (max_pos - min_pos) * (angle / 180.0))

def set_angle(angle):
    servo.duty_u16(angle_to_us(angle))


while True:
    set_angle(0) # Move to 0 degrees
    utime.sleep(1)
    set_angle(90) # Move to 90 degrees
    utime.sleep(1)
    set_angle(180) # Move to 180 degrees
    utime.sleep(1)