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
    #Get Channel
    def getChannel(self):
        return self.getChannel
    #Set Channel
    def setChannel(self, newChannel):
        self.setChannel = newChannel
    #Get Volume
    def getVolume(self):
        return self.getVolume
    #Set Volume
    def setVolume(self, newVolume):
        self.setVolume = newVolume
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

#Test
def TestTV():
    tv1 = TV()
    tv1.setChannel(30)
    tv1.setVolume(3)
    print(tv1.getChannel())
    print(tv1.getVolume())

    tv2 = TV()
    tv2.setChannel(3)
    tv2.setVolume(2)
    print(tv2.getChannel())
    print(tv2.getVolume())

TestTV()