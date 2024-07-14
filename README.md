# π2Go Stick Demos

Welcome to the π2Go Stick demo repository! This repository contains example scripts to help you get started with your π2Go Stick, showcasing the capabilities of this powerful microcontroller tool. The π2Go Stick integrates an RP2040 microcontroller, a button, an LED, two full-color RGB LEDs, and a display, providing a compact and efficient solution for your projects.

## Requirements

To run these demos, you will need:
- A π2Go Stick
- MicroPython installed on the RP2040
- The following drivers:
  - `ssd1312.py` for the display
  - `ws2812.py` for the RGB LEDs

## Demos

### Demo 1: Fade Colors

Source: `demo-fade.py`

This script smoothly transitions the RGB LEDs through various colors. The button on the π2Go Stick toggles the transition on and off.

### Demo 2: Moving Turtle

Source: `moving-turtle.py`

This script demonstrates how to use the internal OLED display to show moving graphics, including text and the π symbol.
