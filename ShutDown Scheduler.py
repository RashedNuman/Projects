from tkinter import *
import os
import subprocess


#==================================================================
#                   BACKEND                                       |
#==================================================================

def shutdown():

    hours = int(e1.get())
    minutes = int(e2.get())

    hours_in_seconds = hours * 3600
    minutes_in_seconds = minutes * 60

    seconds = hours_in_seconds + minutes_in_seconds

    c1 = 'cmd /c '
    c2 = '"shutdown -s -t ' + str(seconds) +'"'
    c3 = c1+c2
    
    os.system(c3)
    
    #os.system('cmd /c "shutdown -s -t 0000"') Format being created

def cancel():
    
  os.system('cmd /c "shutdown -a"')



#=================================================================
#                    FRONTEND                                    |
#=================================================================
  
window = Tk()  
  
window.geometry("400x250")
window.resizable( width = False, height = False)
window.title("Windows ShutDown Scheduler")
  
hours_label = Label(window, text = "Hours").place(x = 30,y = 50)  
  
minutes_label = Label(window, text = "Minutes").place(x = 30, y = 90)

e1 = Entry(window) 
e2 = Entry(window)
e1.pack()
e2.pack()
e1.place(x = 80, y = 50)
e2.place(x = 80, y = 90)


  
sbutton = Button(window, text = "schedule", activebackground = "pink", activeforeground = "blue", command=shutdown)
cbutton = Button(window, text = "Cancel Shutdown schedule", activebackground = "red", activeforeground = "blue", command=cancel) 
  
sbutton.place(x = 30, y = 170)
cbutton.place(x = 180, y = 170)
  
window.mainloop()  
