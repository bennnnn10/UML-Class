import time
from tqdm import tqdm
import tkinter as tk
import pyfiglet

from ClassTV import TV

def turn_on():
    television.destroy()

#Television title using pyfiglet
television_title = pyfiglet.figlet_format("Television", font="starwars", width=100)

television = tk.Tk()
television.title("Television")
television.configure(bg="#F0F0F0")    #Background color
frame = tk.Frame(television, padx=50, pady=50, bg="#F0F0F0")    #Frame
frame.pack()
label = tk.Label(frame, text=television_title, font=("Courier", 24), bg="#F0F0F0")  #Label for television title
label.pack()

#Create button
button = tk.Button(frame, text="Turn On", width=10, height=2, command=turn_on, bg="#FF5500", fg="white")
button.pack(pady=20)

television.mainloop()

#Test Driver Program
def TestTV():

    print("░" * 80)
    print()
    for i in tqdm(range(100), desc="\033[;96;1;3mLoading...\033[0m", ascii=False, ncols=75):
        time.sleep(0.01)
    print()
    print("░" * 80)
    print()
    #Class TV 1
    tv1 = TV()
    #Set TV 1's channel and volume
    tv1.setChannel(30)
    tv1.setVolume(3)
    tv1.turnOn()
    #Print the output
    print(tv1.printStatus().center(93))
    print("■" * 80)
    print("                  tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
    print("■" * 80)
    print()

    print("\n")
    print("░" * 80)
    print()
    for i in tqdm(range(100), desc="\033[;96;1;3mLoading...\033[0m", ascii=False, ncols=75):
        time.sleep(0.01)
    print()
    print("░" * 80)
    print()
    #Class TV 2
    tv2 = TV()
    #Set TV 2's channel and volume
    tv2.setChannel(3)
    tv2.setVolume(2)
    tv2.turnOn()
    #Print the output
    print(tv2.printStatus2().center(93))
    print("■" * 80)
    print("                  tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
    print("■" * 80)
    print()

#For the test cases to be executed, execute the TestTV function.
TestTV()