# gpiUdoo
A simple python library for working with Udoo GPIO

## What is this! A library for ants!?

This little library is intended to take the guesswork out of initilizing pins and reading/writing to them. As of now it doesn't do any SPI I2C or UART but it's decent enough to detect a button press or flash an LED. I'll be adding to it as I go.

Right now it is not even in class form so don't try to do anything with it. I literally made it in 15 minutes. Feel free to watch but as of right now it's not good for use

###Examples

**THIS WILL NOT WORK I AM MAPPING OUT MY EXPECTATIONS**

A simple blink example:

```python
import gpiUdoo
import time

led= gpiUdoo.setup(13,"out")

while True:
	led.write(1)
	sleep(1)
	led.write(0)
	sleep(1)
```