#Tutte le librerie

import sys                         #
from tkinter import *              #
from tkinter import messagebox     #
import tkinter as tk               #  Moduli
import random                      #
from PIL import ImageTk, Image     #
import os                          #
from datetime import datetime      #
import webbrowser                  #
from PyFiles.Lists import *
from PyFiles.Seasons import *
from PyFiles.Operators import *
from PyFiles.RandWindow import *
from PyFiles.MainWindows import *
from PyFiles.Definitions import *


now = datetime.now()
datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")


def DInformazioni():
        Informazioni()
def DStagioni():
        Stagioni()
def DOperatori():
        Operatori()
def DContenuti():
        Contenuti()
def DSoundtrack():
        Soundtrack()
def DRandomizer():
        Randomizer1()
def DElite():
        DEliteS()

def DThermiteElite(event):
    webbrowser.open_new(r"https://www.youtube.com/watch?v=qseVeCbOr8k")        

class Informazioni(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Informazioni')
                self.geometry('400x200')

                self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background7.jpg"))
                self.panel = Label(self, image =self.img)
                self.panel.pack(side = "bottom", fill = "both", expand = "no")
                
                self.iconbitmap(default='Images/Icons/Icon.ico')
                Button(self, text='Stagioni', command = DStagioni).place(y = 10, x = 100)
                Button(self, text='Operatori', command = DOperatori).place(y = 10, x = 250)

                self.mainloop()

class Contenuti(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Contenuti')
                self.geometry('400x200')

                self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background7.jpg"))
                self.panel = Label(self, image =self.img)
                self.panel.pack(side = "bottom", fill = "both", expand = "no")
                
                self.iconbitmap(default='Images/Icons/Icon.ico')
                Button(self, text='Soundtrack', command=DSoundtrack).place(y = 10, x = 100)
                Button(self, text='Schermate Elite', command=DElite).place(y = 10, x = 240)
               

                self.mainloop()


def top():
    window = Toplevel()                                              #  
    window.title('R6S App | 1.006.0')                                #  Configurazione della finestra
    window.geometry('800x700')                                       #
    window.panel = Label(window, text='Scegli cosa vuoi fare')       #  La scritta
    window.panel.pack()
    root.withdraw()                                                  #  Comand per nascondere la schermata iniziale

    window.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background4.jpg"))    #  
    window.panel = Label(window, image=window.img)                   #  Immagine di sfondo
    window.panel.pack(side="bottom", fill="both", expand="no")       #
    window.iconbitmap(default='Images/Icons/Icon.ico')

    m = Menu(root)                                                    #
    context_menu = Menu(root)                                         #
    root.config(menu=m)                                               #
    fn = Menu(m, tearoff=0)
    fn1 = Menu(m, tearoff=0)
    m.add_cascade(label='Info', menu=fn, font='Times 10')             #
    fn.add_command(label='Contatti', command=CInfo)                   #
    m.add_cascade(label='Contatti', menu=fn1)
    fn1.add_command(label='YouTube', command=CYoutube)
    fm = Menu(m, tearoff=0)                                           #
    window.config(menu=m)

    def callback3():
            if messagebox.askokcancel("Uscita", "Sei sicuro di voler uscire?"):
                    window.destroy()
                    root.destroy()

    window.protocol("WM_DELETE_WINDOW", callback3)                

    Button(window, text='Randomizer', command=DRandomizer).place(y = 50, x = 250)      #  Il tasto del reparto Randomizer
    Button(window, text='Informazioni', command=DInformazioni).place(y = 50, x = 450)  #  Il tasto del reparto Randomizer
    Button(window, text='Contenuti', command=Contenuti).place(y = 85, x = 250)
    Button(window, text='Profilo', command=DProfilo).place(y = 570, x = 250)
    Button(window, text='Tactical Board', command=DTacticalBoard).place(y = 570, x = 450)  

    window.mainloop()

#La finestra principale

root = Tk()
root.geometry('800x700')
root.title('R6S App | 1.006.0')
root.iconbitmap(default='Images/Icons/Icon.ico')

w1 = Label(text='Benvenuto in R6S App').pack()

img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Login.jpg"))           #  
panel = Label(root, image = img)                                               #  Immagine di sfondo    
panel.pack(side = "bottom", fill = "both", expand = "no")                      #
 
sd = Label(text="Data:   " + str(now)).place(y = 80, x = 310)

b1 = Button(text='Entra', command = top).place(x = 335, y = 350, width = 130)

root.mainloop()
