import pyautogui
import os
from tkinter import Tk,Button, Entry, Label
import time

#function for screenshot
def Screenshot():

    #get username

    username = os.getlogin()
    file_name = ent1.get()

    #Minimize the window

    window.iconify()
    time.sleep(1)
    myScreenshot = pyautogui.screenshot()

    #save screenshot on desktop

    myScreenshot.save(r'C:\Users\{0}\Desktop\{1}.png'.format(username,file_name))


window=Tk()
window.title("Screenshot Program")
window.geometry('100x100')

btn=Button(window,text="Screenshot",command=Screenshot)
btn.place(x=5,y=35)

global ent1
ent1=Entry(window)
ent1.place(x=75,y=5)

lbl1=Label(window,text="file name:",bg="blue",fg="white")
lbl1.place(x=5,y=5)

window.mainloop()
