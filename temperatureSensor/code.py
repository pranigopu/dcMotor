'''
As we are using library functions, there is not much to do with regard to programming.

First, include the library functions using the import directive:
import Adadfruit_DHT

Second, import the library sys system functions like print:
import sys

Third, import the time library to use timing functions like the function for suspending the sensor for some specified seconds:
import time

Fourth, use the function for taking the sensory inputs read_retry.
The library function read_retry has the syntax:
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
In our case, the sensor is denoted by 11 and the pin is the GPIO (General Purpose Input Output) pin, denoted by 4.
I am not clear with the exact workings, to be honest.
So, the full statement becomes:
humidity, temperature = Adafruit_DHT.read_retry(11,4)

Fifth, place this function in an infinite loop:
while true
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

Now, you can print the retrieved and processed values for temperature and humidity, in the same loop of course:
  print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

To keep a time gap between each loop cycle, use the sleep function from the time library, in the same loop of course:
  time.sleep(1)
(Note that the value passed to sleep is always in seconds)

Hence, the whole code is as follows...
'''

import sys
import Adafruit_DHT
import time
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
    time.sleep(1)