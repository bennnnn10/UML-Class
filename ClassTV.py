#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

class TV:
    #Constructor
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.on = True
    #Turns ON this TV
    def turnOn(self):
        self.on = True
    #Turns OFF this TV
    def turnOff(self):
        self.off = False
    #Print Status
    def printStatus(self):
        if self.on:
            return "\033[;33;1;3mTV 1 is on.\033[0m\n"
        else:
            return "\033[;33;1;3mTV is off.\033[0m\n"
        
    def printStatus2(self):
        if self.on:
            return "\033[;33;1;3mTV 2 is on.\033[0m\n"
        else:
            return "\033[;33;1;3mTV is off.\033[0m\n"
        
    #Get Channel
    def getChannel(self):
        return self.channel
    #Set Channel
    def setChannel(self, newChannel):
        self.channel = newChannel
    #Get Volume
    def getVolume(self):
        return self.volume
    #Set Volume
    def setVolume(self, newVolume):
        self.volume = newVolume
    #Channel Up
    def channelUp(self):
        self.channel += 1
    #Channel Down
    def channelDown(self):
        self.channel -= 1
    #Go to Channel
    def goToChannel(self, channel):
        self.channel = channel
    #Volume Up
    def volumeUp(self, amount):
        self.volume += amount
    #Volume Down
    def volumeDown(self, amount):
        self.volume -= amount