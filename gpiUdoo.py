pins=[116,112,20,16,17,18,41,42,21,19,1,9,3,40,150,162,160,161,158,159,92,85,123,124,125,126,127,133,134,135,136,137,138,139,140,141,142,143,54,205,32,35,34,33,101,144,145,89,105,104,57,56,55,88]
location="/sys/class/gpio/gpio"

def digitalRead(pinNum):
    filename=location+str(pins[pinNum])+"/value"
    f = open(filename, 'r')
    state = int(f.read())
    f.close()
    return state

def getPinDirection(pinNum):
    filename=location+str(pins[pinNum])+"/direction"
    f = open(filename, 'r')
    direction = str.strip(f.read())
    f.close()
    return direction

def setPinDirection(pinNum, direction):
    filename=location+str(pins[pinNum])+"/direction"
    f = open(filename, 'w')
    f.truncate()
    f.write(str(direction))
    f.close()
    return True

def digitalWrite(pinNum,value):
    safecheck=getPinDirection(pinNum)
    if safecheck == "in":
        print(str(pinNum)+" Is currently set as an input. Can't write to it")
        return False
    else:
        filename=location+str(pins[pinNum])+"/value"
        f = open(filename, 'w')
        f.truncate()
        f.write(str(value))
        f.close()
        print("set "+str(pinNum)+" to "+str(value))
	return True

print(setPinDirection(3,"out"))
print(digitalRead(7))
digitalWrite(3,0)
digitalWrite(13,1)
