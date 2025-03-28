import network
import socket
import machine

# Wi-Fi Configuration
SSID = "abi"
PASSWORD = "12345678"

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Wi-Fi Connected! IP:", wlan.ifconfig()[0])

# Initialize UART for Rugged Board Communication
uart = machine.UART(0, baudrate=115200)

# Create a Web Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))  # Listen on port 80
server.listen(5)

print("Server running...")

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode().strip()  # Read request

    print("Received request:", repr(request))  # Debugging

    # Extract only the request path (e.g., "/on/1")
    request_line = request.split("\n")[0]
    path = request_line.split(" ")[1]  # Get the URL path

    # Determine the command to send to Rugged Board
    if path == "/on/1":
        command = "LED_ON_1\n"
    elif path == "/on/2":
        command = "LED_ON_2\n"
    elif path == "/on/3":
        command = "LED_ON_3\n"
    elif path == "/off/1":
        command = "LED_OFF_1\n"
    elif path == "/off/2":
        command = "LED_OFF_2\n"
    elif path == "/off/3":
        command = "LED_OFF_3\n"
    elif path == "/on/blinky":
        command = "LED_ON_BLINKY\n"
    else:
        command = "INVALID\n"

    # Send the command to Rugged Board via UART
    uart.write(command)
    print("Sent to Rugged Board:", command.strip())

    # Send response back to the browser
    html = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n<h1>{command.strip()}</h1>"
    conn.send(html.encode())
    conn.close()

