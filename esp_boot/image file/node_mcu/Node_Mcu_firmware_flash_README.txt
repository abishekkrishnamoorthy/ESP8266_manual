*******************Flash node mcu*********************

sudo apt install python3 python3-pip -y
pip3 install --user esptool
~/.local/bin/esptool.py --version

echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc	
esptool.py --version

sudo pip3 install esptool
wget https://github.com/nodemcu/nodemcu-firmware/releases/latest/download/nodemcu_latest.bin

esptool.py version

python3 -m esptool version

pip3 show esptool

ls /dev/ttyUSB*

esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash
 sudo esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash
 
 
 **wifi firmware files in there***
 
 sudo esptool.py --chip esp8266 --port /dev/ttyUSB0 --baud 115200 write_flash -fm dio -fs 4MB -ff 40m 0x00000 /mnt/data/nodemcu-release-8-modules-2025-03-01-06-17-36-integer.bin	
 
 
 
 
 **After flash completd***
 
 open minicom and add this command for wifi connection 
 
 
 
wifi.setmode(wifi.STATION)
wifi.sta.config({ssid="abi", pwd="12345678"})

tmr.alarm(0, 5000, 1, function()
    if wifi.sta.getip() == nil then
        print("Waiting for IP...")
    else
        print("Connected! IP Address: "..wifi.sta.getip())
        tmr.stop(0)
    end
end)




