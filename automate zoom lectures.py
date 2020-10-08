"""
Description : Automates entering Zoom lectures for your lazy ass

Language : Python 3.8.7

Author : Rashed Numan
co-Author : Komil mamasaliev

Module API : https://github.com/boppreh/keyboard

"""
from pynput.keyboard import Key, Controller
import pyautogui
import keyboard
import os
import time
import sys
import webbrowser
from datetime import datetime as date



def convert24(s, new_timing = ""):

    
   if s[-2:] == "AM" or s[-2:] == "am" :
       
      if s[:2] == '12':
        
          a = str('00' + s[2:5])
          
      else:
          
          new_timing = s[:-2]
   else:
       
      if s[:2] == '12':
          
          new_timing = s[:-2]
          
      else:
          
          new_timing = str(int(s[:2]) + 12) + s[2:5]
          
   return new_timing

  



def join_lecture(code):

    """
    DOESNT RETURN SHIT ONLY EXECUTES
    """

    if len(code) > 11: # link
        webbrowser.open(code)
        time.sleep(1)
        keyboard.press_and_release("tab")
        keyboard.press_and_release("tab")
        time.sleep(0.5)
        keyboard.press_and_release("enter")
    


    else: # code 
        keyboard.press_and_release("win")
        time.sleep(0.5)
        keyboard.write("start zoom")
        time.sleep(0.5)
        keyboard.press_and_release("enter")
        time.sleep(0.5)

        pyautogui.leftClick(x=816, y=396) # join


        time.sleep(0.2)
        keyboard.write(code)
        time.sleep(0.2)
        keyboard.press_and_release("enter")
        

    time.sleep(6)
    pyautogui.leftClick(x=951, y=526) # join audio\
    time.sleep(0.5)
    pyautogui.leftClick(x=951, y=526)
    time.sleep(2)
    
    Controller.press(Key.alt)
    Controller.type("h")

    Controller.type("sup niggas")
    #pyautogui.leftClick(x=907, y=931) # open chatbox
    #time.sleep(0.5)
    #pyautogui.leftClick(x=855, y=667) # click chat

    keyboard.write("im here nigga")
    keyboard.press_and_release("enter")
    return None


lectures = dict()

with open("ZOOMED.txt") as file:

    for line in file:

        print(line)
        record = line.strip("\n")
        lecture = record.split("-")
        timing = convert24(lecture[0])
        
        code = lecture[1]
       
        lectures[timing] = code

        
print(lectures)

while True:

    #time.sleep(30)

    current_time = date.now()

    for timing in lectures.keys():
        
        if current_time.strftime("%H:%M") == timing:

            join_lecture(lectures[timing])
            time.sleep(60)
            


