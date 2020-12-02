# About
Mid Altitude Meteorological Balloon Apparatus - This is a project that seeks to launch an Arduino controlled weather balloon to an altitude of 40,000 feet and collect weather data
# Hardware
To be added
# Dependencies
## Arduino
You must install the [Arduino IDE](https://downloads.arduino.cc/arduino-1.8.13-windows.exe) to compile and flash the .ino file to the Arduino
```Arduino_LPS22HB.h```
```Arduino_HTS221.h```
```Adafruit_GPS.h```
They can be installed from the Arduino IDE via ```Tools > Manage Libraries``` or with the keyboard shortcut ```Ctrl+Shift+I```
## Python
Python 3 and the Python library ```serial``` must be installed if you choose to use the included receiver software. Install the library by typing ```pip install serial```in your computer's command line. If you get the message ```'pip' is not recognized as an internal or external command,
operable program or batch file.```, it is likely due to Python not being in the PATH variable, so make sure to check **Add to PATH** when installing Python
# How to use
## Reciever Software
Once all the dependencies have been installed, Connect the TTL to USB interface to your PC, and open up the Arduino IDE. Make sure the Arduino *is not* plugged in to the PC. Once it's plugged in, in the Arduino IDE navigate to ```Tools > Port```, and write down the exact name of the port that shows up. Then, in the ```Reciver Software.py```, replace ```COM9``` in line 4 with the name of the port. ```COM9``` is the port on my computer, but it is different from device to device. 
## Arduino
In the Arduino IDE, navigate to ```Tools > Board > Boards Manager``` and install ```Arduino nRF528x Boards (Mbed OS)```. Then navigate to ```Tools > Board > Arduino nRF528x Boards (Mbed OS)``` and select ```Arduino Nano 33 BLE```. Plug in the Arduino via a Micro USB cable, and under ```Tools > Port``` select the port that has the name of the board next to it. Then, upload the sketch to the Arduino, and it should begin working.
