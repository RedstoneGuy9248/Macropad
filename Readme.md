# Ridhim's Macropad
Ridhim's Macropad is a 9-key macropad with a EC11 rotary encoder running on an RPi Pico. (Made for Hack Club Fallout)

## Features:
- Cool looking case
- EC11 Rotary Encoder as a volume knob
- 9 Keys (Reprogrammable in Python)
- Connects using Micro-USB

### why?
I made this project as a bit of a more complex next project, compared to my [previous hardware project](https://github.com/RedstoneGuy9248/weatherStation), as i barely have any hardware experience and need practice to be able to build actual complex ones. (also for fallout lol). From this, I've learnt the basics of how to design PCBs in KiCAD, re-learnt Fusion 360 after like 4 years, and also understood a lot about how hardware made to like actual complete products are made. 

![Image of macropad fully assembled](/assets/Assembly.png)

## Assembly:
- Snap the switches into the plate
- Then the switches, diodes, rotary encoder, and RPi Pico should be soldered onto the pcb acccording to the schematic. 
- Place the plate with the pcb attached underneath it into the base and fit the micro usb port into its hole
- Place the top part, and then insert 4 M3*20mm screws into the holes and secure underneath with nuts
- Insert keycaps onto switches and dial onto rotary encoder

## Setup
- [Install CircuitPython on the RPi Pico](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
- Get an up to date copy of [KMK](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/main.zip)
- Unzip it and drag the contents into the root of the usb drive corresponding to the RPi Pico
- Copy the main.py file from firmware/ of this repo into the same root folder

## Schematic

![Image of macropad schematic](/assets/Schematic.png)

## PCB

![Image of macropad PCB Flat](/assets/PCB%202D.png)
![Image of macropad PCB 3D](/assets/PCB%203D.png)
![Image of macropad PCB 3D Underside](/assets/PCB%20Underside.png)

## Bill Of Materials

The BOM is available [here](/BOM.csv)

## Zine

![Image of Zine](/assets/Zine.png)

(The pdf is available [here](/Ridhim%27s%20Macropad%20Zine.pdf))

## Note:

There are 2 variants of the plate available, one has a thickness of 1.5mm and the other is 3mm. The 3mm is the main one as it is the size specified in the Hackpad guide, and a 1.5mm 3D Printed plate would be very fragile.
