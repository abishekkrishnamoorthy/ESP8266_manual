import network
import machine
import time
import os

# Wi-Fi Credentials
SSID = "abi"
PASSWORD = "12345678"

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

print("Connecting to Wi-Fi...", end=" ")
timeout = 10  # 10-second timeout

while not wifi.isconnected() and timeout > 0:
    print(".", end="")
    time.sleep(1)
    timeout -= 1

if wifi.isconnected():
    print("\nWi-Fi Connected! IP:", wifi.ifconfig()[0])
else:
    print("\nWi-Fi Connection Failed. Check SSID/Password.")

# Initialize UART (for Rugged Board communication)
uart = machine.UART(0, baudrate=115200)  # TX=GPIO1, RX=GPIO3
print("UART Initialized")

print("boot.py execution completed")

# Run main.py
try:
    print("Starting main.py...")
    import main  # This runs main.py automatically
except Exception as e:
    print("Error running main.py:", str(e))

