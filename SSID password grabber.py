"""

                        SSID password Extractor

@Author : Rashed Alnuman
@Author : Komil mamasaliev

Language : Python3

Description : uses cmd to get the key for all SSID stored on device

"""

import os
import _thread
import subprocess
from time import sleep as nap
import re
from tkinter import *
import winsound

#############################################################################
#                           Back End                                        #
#############################################################################


def grab_pass():
    command = "netsh wlan show profile"
    test1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    test1_return = test1.stdout.read()
    SSID_output = str((test1_return))
    unfiltered_id = SSID_output[195:].split(":")

    size = len(unfiltered_id)

    for index in range(size):

        if index == size - 1:
            unfiltered_id[index] = unfiltered_id[index][:-9].lstrip(" ")

        else:
            unfiltered_id[index] = unfiltered_id[index][:-29].lstrip(" ")

    filtered_id = unfiltered_id

    size2 = len(filtered_id)
    passwords_list = []
    for i in range(size2):

        command2 = "netsh wlan show profile " + filtered_id[i] + " key=clear"
        test2 = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE)
        test2_return = test2.stdout.read()
        result2 = str((test2_return))
        # print("\n \n")

        if i == size2 - 1:

            password = result2[1170:].split("\\")[0]
            # print(filtered_id[i] + "pass -> " + password)
            passwords_list.append( str(i+1) + ": " + filtered_id[i] + " pass -> " + password + "\n")

        else:
            password = result2[1159:].split("\\")[0]
            # print(filtered_id[i] + "pass -> " + password)
            passwords_list.append( str(i+1) + ": " + filtered_id[i] + " pass -> " + password + "\n")

    """ Converting the password list to string """
    passwords_list_str = ""

    for elements in passwords_list:
        passwords_list_str += elements

    return passwords_list_str



#############################################################################
#                           FRONT END                                       #
#############################################################################



def button_grab_func():
    output_text.config(state="normal")  # setting the text back to editable
    new_text = grab_pass()
    output_text.delete("1.0", END)  # Delete the written text
    output_text.insert(1.0, new_text)  # Set new text for the password
    output_text.config(state=DISABLED)  # Setting it back to un-editable




# The Tkinter
root = Tk()

""" Create the beeping sound """
frequency = 1500 # setting the freq to 1500 Hz
duration = 250 # setting the duration to 250 ms, 1/4 of a sec

# winsound.Beep(frequency,duration) Use this command to make the sound

""" Geometry of the window """
root.geometry("600x515")
root.resizable(0, 0)  # Fix the size
root.pack_propagate(0)  # Setting the size to not move after packing
root.title("Password Grabber")

""" Declaring the variables """
welcome = StringVar()
GRAB = StringVar()
password_output = StringVar()

""" Setting the variables """
welcome.set("Welcome to the GRAB")
GRAB.set("GRAB")

""" Creating the stuFF """
label1 = Label(root, width=0, font=("Arial", 20), textvariable=welcome)

output_text = Text(root, width=50, height=18.5, background="yellow", font=("Arial", 12), wrap=WORD)
output_text.insert(1.0, "The password's will show here. (Please press the GRAB button)")

button_grab = Button(root, width=0, font=("Arial", 20), textvariable=GRAB, command=button_grab_func, background="green")


scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=output_text.yview)
output_text.config(state=DISABLED)  # setting it to un-editable

""" Packing/positioning the stuFF """
label1.place(x=150, y=20)
button_grab.place(x=220, y=100)
output_text.place(x=80, y=165)




root.mainloop()
