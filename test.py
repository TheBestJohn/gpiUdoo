from gpiUdoo import gpiUdoo

switch = gpiUdoo(13,"in")
led = gpiUdoo(12,"out")
print(switch.digitalRead())