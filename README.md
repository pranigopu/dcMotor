# DC Motor controlled using Raspberry Pi
Controlling a DC motor using Raspberry Pi and Python.

## Requirements
- Raspberry Pi
- L298N Motor Driver Module
- 12V DC Motor
- 12V Power Supply for Motor and Motor Driver
- Power Supply for Raspberry Pi
- Connecting Wires

## Physical setup
### Preliminary notes 1
I am using the L298N motor driver. Ports for each motor:

- Motor 1: OUT1, OUT2, ENA, IN1, IN2
- Motor 2: OUT3, OUT4, ENB, IN3, IN4

Descriptions:

- OUT: For providing signals to the motor so it can run as specified.
- EN: (Enabler) For allowing the motor to recieve a amount of power specified through the microcontroller*.
- IN: For taking signals from the microcontroller* to control the motor's direction (in this case our Raspberry Pi)

### Preliminary notes 2
- IN(i) = IN(i + 1) => Motor is still
- IN(i) = HIGH & IN(i + 1) = LOW => Rotation in a specific direction
- IN(i) = LOW & IN(i + 1) = HIGH => Rotation in the opposite direction

### Terminology
- GND: Ground
- GPIO: General Purpose Input Output (pin / terminal)

Setup
1. Connect 12V power source to  L298N Motor Driver Module.
2. Connect GND pin of L298N to GND pin of Raspberry Pi.
For motor 1:
3. Connect the ENA pin of L298N to Physical Pin 22 (GPIO25) of Raspberry Pi.
4. Connect the IN1 and IN2 of L298N Module to Physical Pins 16 and 18 (GPIO23 and GPIO24) of Raspberry Pi.
