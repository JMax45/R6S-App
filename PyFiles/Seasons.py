import sys
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def DChimera():
        Chimera()

class Chimera(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Chimera')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Chimera\Chimera.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DWhiteNoise():
        WhiteNoise()

class WhiteNoise(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('White Noise')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\White Noise\WhiteNoise.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DBloodOrchid():
        BloodOrchid()

class BloodOrchid(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Blood Orchid')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Blood Orchid\BloodOrchid.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DOperationHealth():
        OperationHealth()

class OperationHealth(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Operation Health')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Operation Health\OperationHealth.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()      
                

def DVelvetShell():
        VelvetShell()

class VelvetShell(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Velvet Shell')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Velvet Shell\VelvetShell.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DRedCrow():
        RedCrow()

class RedCrow(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Red Crow')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Red Crow\RedCrow.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DSkullRain():
        SkullRain()

class SkullRain(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Skull Rain')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Skull Rain\SkullRain.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DDustLine():
        DustLine()

class DustLine(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Dust Line')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Dust Line\DustLine.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DBlackIce():
        BlackIce()

class BlackIce(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Black Ice')
                self.geometry('500x400')

                img = ImageTk.PhotoImage(Image.open("Images\Images\Informations\Seasons\Black Ice\BlackIce.jpg"))           
                panel = Label(self, image = img)                                                   
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()       
