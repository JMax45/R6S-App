import webbrowser
import sys
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image 

def callback3(event):
    webbrowser.open_new(r"https://www.youtube.com/channel/UC7qTuN4j9Cgjvcu38CsrBqA")

def callback(event):
    webbrowser.open_new(r"https://www.youtube.com/channel/UC7qTuN4j9Cgjvcu38CsrBqA")

def callback2(event):
    webbrowser.open_new(r"https://www.youtube.com/channel/UCfHjEQNvOjb0Y8FUyrzJjng")

def DProfilo():
    webbrowser.open_new(r"https://rainbow6.ubisoft.com/siege/en-us/player-activities/index.aspx")
def DTacticalBoard():
    webbrowser.open_new(r"https://rainbow6.ubisoft.com/siege/en-us/whiteboard/landing.aspx")    
    
def CYoutube():
    window2 = Toplevel()                                                     
    window2.title('Contatti')                                                
    window2.geometry('700x150')                                              
    window2.iconbitmap(default='Images/Icons/Icon.ico')

    Label(window2, text="Qui potete trovare i nostri canali YouTube").pack() 

    Link1 = Label(window2, text="JMax", fg="blue", cursor="hand2")           
    Link1.pack()                                                               
    Link1.bind("<Button-1>", callback)                                       

    Link2 = Label(window2, text="Zever", fg="blue", cursor="hand2")          
    Link2.pack()                                                               
    Link2.bind("<Button-1>", callback2)                                      

    window2.mainloop()
