# Temperature Sensor using Raspberry Pi

A small project to interface a temperature and humidity sensor with Raspberry Pi

## Digital setup
We need to download and install a library called `Adafruit_DHT`, provided by Adafruit, into our Raspberry Pi.

**NOTE**: _All the following actions are to be done in the terminal, unless stated otherwise._

---

First, download the library from GitHub. It helps organise your workspace  if you create a folder to place the library in.

Second, download the files related to the library using the command:

```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
```

All the files downloaded through this will be stored in a directory called `Adafruit_Python_DHT`.  You can open this directory through the terminal using:

```
cd Adafruit_Python_DHT
```

---

Third, if you open the directory Adafruit_Python_DHT, you can find a file named `setup.py`. Install this file using the command:

```
sudo python setup.py install
```

**SIDE NOTE**: `sudo` _('superuser do') is a command that allows you to run programs with the security privileges of another user. This is by default the superuser / admin_