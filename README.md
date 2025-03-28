# 🌟 **ESP8266 Module Manual** 🚀

Welcome to the **ESP8266 Module Manual**, your ultimate guide to flashing, booting, and accessing the ESP8266 Wi-Fi module!

---

## 🔥 **How to Flash**

1. Connect your ESP8266 to your computer using a USB-to-serial adapter.
2. Download and install **esptool.py** or **NodeMCU Flasher**.
3. Put the ESP8266 in **flash mode** by pressing the **GPIO0** button while resetting.
4. Run the following command:

   ```bash
   esptool.py --port /dev/ttyUSB0 write_flash 0x00000 firmware.bin
   ```
5. Wait for the flashing process to complete and restart the module.

---

## ⚡ **How to Boot**

ESP8266 has three boot modes:

- **Normal Boot** 🟢 – Boots the firmware normally.
- **Flash Mode** 🔵 – Used for uploading firmware.
- **UART Boot** 🔴 – Debugging mode.

| Boot Mode  | GPIO0 | GPIO2 | GPIO15 |
|------------|-------|-------|--------|
| Normal Boot | 1 | 1 | 0 |
| Flash Mode | 0 | 1 | 0 |
| UART Boot | 1 | 0 | 0 |

Set the pins accordingly to enter the desired mode.

---

## 🌐 **How to Access**

1. Connect to the ESP8266 using **serial communication**:
   ```bash
   screen /dev/ttyUSB0 115200
   ```

2. Use **AT commands** to check the module:
   ```bash
   AT
   AT+CWLAP  # List available Wi-Fi networks
   AT+CWJAP="SSID","PASSWORD"  # Connect to Wi-Fi
   ```

3. Access the ESP8266 **via Web Server**:
   - Upload an HTTP server firmware.
   - Connect to the ESP8266’s IP (default **192.168.4.1** in AP mode).

---

### 🎯 **Stay Connected!**

💬 Need help? Join our community discussions! 🚀

🔗 **[Official ESP8266 Documentation](https://espressif.com/)**  
📌 **[GitHub Repo](https://github.com/your-repo-link)**

🌍 Happy Hacking! 😃
