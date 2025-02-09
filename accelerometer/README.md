# Accelerometer using Raspberry Pi
## Requirements
- Raspberry Pi + Micro SD card
- ADXL345 accelerometer
- Breadboard wire
- Power supply

## Physical setup
Terminology:

- GND: Ground.
- VCC: Voltage Common Collector.
- I2C: Inter-Integrated Circuit.
- SDA: Serial Data. 
- SCL: Serial Clock.

---

Setup procedure:

1. Wire GND pin in accelerometer to Physical Pin 6 (GND) in Raspberry Pi
2. Wire VCC pin in accelerometer to Physical Pin 1 (3V3 i.e. 3.3 Volts Pin) in Raspberry Pi
3. Wire SDA pin in accelerometer to Physical Pin 3 (SDA) in Raspberry Pi
4. Wire SCL pin in accelerometer to Physical Pin 5 (SCL) in Raspberry Pi

## Digital setup
Before getting our Raspberry Pi to retrieve data from the accelerometer, we must make sure that:

1. Our Raspberry Pi's software is up-to-date
2. Enable I2C in the Raspberry Pi <br> (see [physical setup](#physical-setup) to know more about I2C)

**NOTE**: _All the following actions must be done through the terminal unless stated otherwise._

---

### 1. Making Raspberry Pi's software is up-to-date
Use the following commands to update and upgrade the Raspberry:

```
sudo apt-get update
sudo apt-get upgrade
```

### 2. Enabling I2C in the Raspberry Pi 
First, after having updated and upgraded the Raspberry, launch the Raspberry's configuration tool to enable I2C in the Raspberry:

```
sudo raspi-config
```

**NOTE**: `sudo` _('superuser do') allows you to run programs with the security privileges of another user, by default the superuser / admin._

---

Second, you will get a menu of options. Navigate using arrow keys. Go to Interfacing Options, which is option 5. Press enter to select.

---

Third, in the Interfacing Options menu, select the option P5 I2C.
When asked to enable ARM I2C interface, select yes.

---

Fourth, having enabled the I2C interface in the Raspberry, restart the Raspberry using:

```
sudo reboot
```

---

Fifth, having restarted the Raspberry, we must install the packages needed to interact with the accelerometer using:

```
sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y
```

---

Sixth, having installed the necessary packages, we can test whether the Raspberry can actually detect the accelerometer. To do this, use:

```
sudo i2cdetect -y 1
```

You must get some output. If nothing appears then make sure you have connected your ADXL345 accelerometer to the Raspberry correctly. Also check that all solder points on the pins of the sensor are clean. If you see an error, try re-enabling I2C again.