import time

import pyautogui
from pyautogui import *
import tkinter as Tk
from tkinter import *

wind = Tk()
wind.geometry("450x100")
wind.resizable(False,False)
wind.title("Alternative of pyautogui.displayMousePosition()")
Lb = Label(wind, text = "Loading" ,font = ("Courier" ,13 ,'bold'))
Lb.pack()
while True:
    x ,y = pyautogui.position()
    r ,g ,b = pyautogui.pixel(x,y)[0],pyautogui.pixel(x,y)[1],pyautogui.pixel(x,y)[2]
    Lb["text"] = f"({x} ,{y}) ,rgb : {r} ,{g} ,{b}"
    wind.update()

