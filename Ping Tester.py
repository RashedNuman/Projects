from tkinter import *
import tkinter as tk
import tkinter.font as font
import io
import os
import subprocess
import _thread
from time import sleep
from datetime import date

#=====================================================================================
# FRONT END OF THE PROGRAM
#=====================================================================================

window = Tk()
window.geometry("600x400")
window.resizable( width = False, height = False)
window.title("League Ping Tester")

title = tk.Label(text = " Ping Tester")

subTitle = tk.Label(text = "Check Your Ping ")

version = tk.Label(window, text = "VERSION -alpha 0.7-")

frame1 = Frame(window)

pingResults = """EW = 130ms
EUNE = 120ms
NA = 145ms
"""
             
test1 = tk.Label(frame1, text = pingResults)


title.config(font = ("Courier", 25))
test1.config(font = ("Times", 20))

title.pack()
subTitle.pack()

test1.pack(side = tk.LEFT, pady = 30)

version.place(relx = 0.0, rely = 1.0, anchor = "sw")
frame1.place(relx = 0.5, rely = 0.5, anchor = "center")



#=====================================================================================
# BACK END OF THE PROGRAM
#=====================================================================================
def ping_test(name, address):

    global subprocess
    global command

    file = open("Ping Results.txt", "a+")
    command = "ping " + address + " -4"
    subprocess = subprocess.Popen( command, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    result = str(subprocess_return)

    ping = name + " Current ping = " + result.split(" ")[-1][0:5]

    if ping == "LOSS)" or ping == "loss)":
        
        file.write("Could not establish connection... \n")
        file.close()      
    else:
     
        file.write(ping + "\n")
        file.close()

    print("Operation Done")



eu = _thread.start_new_thread( ping_test, ("EUNE", "104.160.142.3",))
ew = _thread.start_new_thread( ping_test, ("EUW", "104.160.141.3",))
na = _thread.start_new_thread( ping_test, ("NA", "104.160.131.1",))
oce = _thread.start_new_thread(ping_test, ("OCE", "104.160.156.1",))
lan = _thread.start_new_thread(ping_test, ("LAN", "104.160.136.3",))

print("done")


#os.system('cmd /k "e"')

window.mainloop()
