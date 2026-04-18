# Ridhim's Macropad
Ridhim's Macropad is a 9-key macropad with a EC11 rotary encoder running on an rpi pico.

## Features:
- Cool looking case
- EC11 Rotary Encoder as a volume knob
- 9 Keys (Reprogrammable in Python)

## Assembly:
- Snap the switches into the plate
- Then the switches, diodes, rotary encoder, and rpi pico should be soldered onto the pcb acccording to the schematic. 
- Place the plate with the pcb attached underneath it into the base and fit the micro usb port into its hole
- Place the top part, and then insert 4 M3*20mm screws into the holes and secure underneath with nuts
- Insert keycaps onto switches and dial onto rotary encoder

## Setup
- [Install CircuitPython on the RPi Pico](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
- Get an up to date copy of [KMK](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/main.zip)
- Unzip it and drag the contents into the root of the usb drive corresponding to the RPi Pico
- Copy the main.py file from KMK_Firmware/ of this repo into the same root folder
