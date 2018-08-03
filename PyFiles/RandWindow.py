import sys
from tkinter import *
import tkinter as tk
import random
from PIL import ImageTk, Image
import os
from PyFiles.Lists import *


def wpronostico():
        Child()
def spawn():
        Spawn()
def mirino():
        Mirino()

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_child()

    def scelta(self):
        tk.Label(self, text='' + random.choice(code_list3)).place(x = 87, y = 110)
           
    def init_child(self):
        self.title('Pronostico')
        self.geometry('200x200')
        self.iconbitmap(default='Images/Icons/Icon.ico')
        tk.Button(self, text='Vincerai?', command=self.scelta).pack()
        self.mainloop()

class Spawn(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def spawn2(self):
                self.label_text.config(text='' + random.choice(code_list4))
                return

        def init_child(self):
                self.title('Spawn')
                self.geometry('200x200')
                self.iconbitmap(default='Images/Icons/Icon.ico')
                self.label_text = tk.Label(self, text='' + random.choice(code_list4))
                self.label_text.place(x=92, y=110)
                tk.Button(self, text='Spawn', command=self.spawn2).pack()
                self.mainloop()

class Mirino(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def mirino2(self):
                self.label_text.config(text=''+random.choice(code_list5))
                return

        def init_child(self):
                self.title('Mirino')
                self.geometry('200x200')
                self.iconbitmap(default='Images/Icons/Icon.ico')
                self.label_text = tk.Label(self, text='' + random.choice(code_list5))
                self.label_text.place(x=82, y=110)
                tk.Button(self, text='Mirino', command=self.mirino2).pack()
                self.mainloop()

                
        
