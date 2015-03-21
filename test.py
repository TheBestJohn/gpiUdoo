from gpiUdoo import gpiUdoo
import time

switch = gpiUdoo(13,"in")
led = gpiUdoo(12,"out")
print(switch.digitalRead())


while True:
	led.digitalWrite(1)
	time.sleep(1)
	led.digitalWrite(0)
	time.sleep(1)
