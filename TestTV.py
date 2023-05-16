from ClassTV import TV

#Test Driver Program
def TestTV():
    #Class TV 1
    tv1 = TV()
    #Set TV 1's channel and volume
    tv1.setChannel(30)
    tv1.setVolume(3)
    tv1.turnOn()
    #Print the output
    print(tv1.printStatus())
    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
    print()

    #Class TV 2
    tv2 = TV()
    #Set TV 2's channel and volume
    tv2.setChannel(3)
    tv2.setVolume(2)
    tv2.turnOn()
    #Print the output
    print(tv2.printStatus2())
    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
    print()

#For the test cases to be executed, execute the TestTV function.
TestTV()