from machine import UART, Pin
from time import sleep
from re import match

uart = UART(0, baudrate=115200, tx=Pin("GP16"), rx=Pin("GP17"))

def send_at_command(command):
    uart.write(command + '\r\n')
    sleep(2) # Wait for response
    response = uart.read() # Read the response
    return response.decode() if response else None

def make_call(number):
    response = send_at_command('ATD{};'.format(number))
    print(f"Response: {response}")
    if response and not ("OK" in response):
        print("Failed to make the call")
        return
    print(f"Call placed to {number}")

def test_connection():
    response = send_at_command('AT')
    print(response)
    if response and ('OK' in response):
        print("A9G module is properly connected.")
        return True
    else:
        print("A9G module is not properly connected or not responding.")
        return False

make_call("0714453474")