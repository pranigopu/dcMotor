'''
For the code, we will be using ready-made libraries.

(Note: all the following actions are to be done through the terminal unless stated otherwise)

First, we must download and install Adafruit's ADXL34x Python library. 
To install it so we can use it, use:
sudo pip3 install adafruit-circuitpython-ADXL34x

------------

Second, having installed the ADXL34x Python library, we can start with our code.
You can write through the terminal itself using:
nano ~/accelerometer.py
(accelerometer.py is a new file. You can give any name, but suffix by .py since it is to be a Python script)

------------

Third, include the following libraries in the code:
time - enables time related functions like putting the script on hold for a specified duration.
board - to quickly know the correct pins for the microcontroller, which is in this case our Raspberry Pi.
busio - (bus input output) contains libraries capable of handling various serial protocols, which allows us to handle the I2C.
        (Serial implies transmission of data one bit at a time through a single channel)
adafruit_adxl34x - contains all the code needed for reading information from our ADXL345 accelerometer.

------------

Fourth, we prepare an I2C connection for our current board pins SDA and SCL using a function from busio.
We store the handle of this connection to a variable we shall call i2c.
(
  Side notes: 
  A handle: an abstract referrence to a resource.
            It is abstract since it must be processed to become something the processor can handle as intended.
  A referrence: a value that allows a program to indirectly access a datum, like a variable's value, address, or a process' address
  A resource is any physical or virtual component of limited availablilty.
)
The statement is:
i2c = busio.I2C(board.SCL, board.SDA)

------------

Fifth, we now instantiate the ADXL345 library into an object we shall call accelerometer. 
(
  Instantiate: make an instance of.
  Here, the ADXL345 library is a class, and we make an instance of this class
)
We will utilize this object to read and obtain information from our sensor. 
Into the constructor for the library, we pass in our I2C handle so it can access and use the established connection.
The statement is:
accelerometer = adafruit_adxl34x.ADXL345(i2c)

------------

Sixth, Here we start an infinite loop by using while True:.
Within this infinite loop, we print out the X, Y, and Z acceleration values.
(Note that these values have been retrieved from the accelerometer by the library)
Once we have printed the X, Y, and Z values, we then put the script to sleep for half a second.
(We sleep the script to stop it from flooding the command line with the values provided by the accelerometer)
 The statements are:
 while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(0.5)

------------

The final script:
'''

import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)

'''
Finally, save the code by pressing CTRL + X then Y followed by ENTER.
Run the script using:
python3 ~/accelerometer.py
'''