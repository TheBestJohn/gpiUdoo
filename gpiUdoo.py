pins=[116,112,20,16,17,18,41,42,21,19,1,9,3,40,150,162,160,161,158,159,92,85,123,124,125,126,127,133,134,135,136,137,138,139,140,141,142,143,54,205,32,35,34,33,101,144,145,89,105,104,57,56,55,88]
location="/sys/class/gpio/gpio"

class gpiUdoo:
    def __init__(self, pin, io):
        self.pin = pins[pin]
        if io != "in" and io != "out":
            return False
        else:
            setPinDirection(io)
            print(str(io)+str(pins[pin]))

    def digitalRead(self):
        filename=location+str(self.pin)+"/value"
        f = open(filename, 'r')
        state = int(f.read())
        f.close()
        return state

    def getPinDirection(self):
        filename=location+str(self.pin)+"/direction"
        f = open(filename, 'r')
        direction = str.strip(f.read())
        f.close()
        return direction

    def setPinDirection(self, direction):
        filename=location+str(self.pin)+"/direction"
        f = open(filename, 'w')
        f.truncate()
        f.write(str(direction))
        f.close()
        return True

    def digitalWrite(self,value):
        if getPinDirection() == "in":
            print(str(self.pin)+" Is currently set as an input. Can't write to it")
            return False
        else:
            filename=location+str(self.pin)+"/value"
            f = open(filename, 'w')
            f.truncate()
            f.write(str(value))
            f.close()
            print("set "+str(self.pin)+" to "+str(value))
            return True
