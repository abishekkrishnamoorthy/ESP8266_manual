import network
import time

# WiFi credentials
SSID = "abi"        # Replace with your Wi-Fi SSID
PASSWORD = "12345678"  # Replace with your Wi-Fi password

# Initialize Station (STA) mode
wifi = network.WLAN(network.STA_IF)  
wifi.active(True)  # Activate WiFi

# Connect to Wi-Fi
if not wifi.isconnected():
    print("Connecting to WiFi...")
    wifi.connect(SSID, PASSWORD)

    # Wait for connection
    timeout = 10  # Timeout in seconds
    while not wifi.isconnected() and timeout > 0:
        print("Waiting for connection...")
        time.sleep(1)
        timeout -= 1

# Check connection status
if wifi.isconnected():
    print("Connected!")
    print("IP Address:", wifi.ifconfig()[0])  # Print assigned IP
else:
    print("Failed to connect. Check credentials.")

