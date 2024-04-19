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
    
    if response and ("OK" not in response):
        print("Failed to make the call")
        return
    print(f"Call placed to {number}")

def send_sms(number, text):
    response = send_at_command("AT+CMGF=1")

    if not response or ("OK" not in response):
        print("Failed to set SMS format")
        return
    
    response = send_at_command(f'AT+CMGS="{number}"')
    if not response or (">" not in response):
        print("Failed to set recipient number")
        return
    
    response = send_at_command(text)
    if not response:
        print("Failed to send message.")
        print(f"Response: {response}")
        return
    
    print(f"Response (success) : {response}")
    
    uart.write(chr(26))
    sleep(1)

def receive_sms():
    response = send_at_command("AT+CMGF=1")
    if not response or ("OK" not in response):
        print("Failed to set SMS format")
        return

    response = send_at_command('AT+CMGL="ALL"')
    print(response)

def delete_sms():
    response = send_at_command('AT+CMGDA="DEL ALL"')
    print(response)

def test_connection():
    response = send_at_command('AT')
    if response and ('OK' in response):
        print("A9G module is properly connected.")
        return True
    else:
        print("A9G module is not properly connected or not responding.")
        return False

def gps_read():
    print(send_at_command("AT+GPS=1"))

    # print(send_at_command("AT+GPSRD=1"))
    gps_data = send_at_command("AT+LOCATION=1")
    
    return gps_data
