import sys
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def DLyon():
        Lyon()

class Lyon(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Lyon')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GIGN/Lyon.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DFinka():
        Finka()

class Finka(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Finka')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/Spetsnaz/Finka.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DVigil():
        Vigil()

class Vigil(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Vigil')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/707 SMB/Vigil.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DDokkaebi():
        Dokkaebi()

class Dokkaebi(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Dokkaebi')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/707 SMB/Dokkaebi.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DZofia():
        Zofia()

class Zofia(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Zofia')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GROM/Zofia.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DYing():
        Ying()

class Ying(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Zofia')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SDU/Ying.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DJackal():
        Jackal()

class Jackal(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Jackal')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GEO/Jackal.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DHibana():
        Hibana()

class Hibana(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Hibana')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SAT/Hibana.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DCapitao():
        Capitao()

class Capitao(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Capitao')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/BOPE/Capitao.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()                    

def DBlackbeard():
        Blackbeard()

class Blackbeard(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Blackbeard')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SEALS/Blackbeard.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DBuck():
        Buck()

class Buck(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Blackbeard')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/JTF2/Buck.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DSledge():
        Sledge()

class Sledge(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Sledge')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SAS/Sledge.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DThatcher():
        Thatcher()

class Thatcher(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Thatcher')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SAS/Thatcher.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DAsh():
        Ash()

class Ash(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Ash')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/FBI/Ash.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DThermite():
        Thermite()

class Thermite(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Thermite')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/FBI/Thermite.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DTwitch():
        Twitch()

class Twitch(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Twitch')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GIGN/Twitch.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DMontagne():
        Montagne()

class Montagne(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Montagne')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GIGN/Montagne.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DBlitz():
        Blitz()

class Blitz(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Blitz')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GSG/Blitz.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DIQ():
        IQ()

class IQ(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('IQ')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GSG/IQ.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()                                  

def DFuze():
        Fuze()

class Fuze(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Fuze')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/Spetsnaz/Fuze.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()                                  

def DGlaz():
        Glaz()

class Glaz(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Glaz')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/Spetsnaz/Glaz.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()                                  

                
def DEla():
        Ela()

class Ela(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Ela')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GROM/Ela.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DLesion():
        Lesion()

class Lesion(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Lesion')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SDU/Lesion.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DMira():
        Mira()

class Mira(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Mira')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GEO/Mira.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DEcho():
        Echo()

class Echo(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Echo')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SAT/Echo.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DCaveira():
        Caveira()

class Caveira(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Caveira')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/BOPE/Caveira.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DValkyrie():
        Valkyrie()

class Valkyrie(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Valkyrie')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SEALS/Valkyrie.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DFrost():
        Frost()

class Frost(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Frost')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/JTF2/Frost.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()               

def DMute():
        Mute()

class Mute(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Mute')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SAS/Mute.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DSmoke():
        Smoke()

class Smoke(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Smoke')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/SAS/Smoke.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()                               

def DCastle():
        Castle()

class Castle(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Castle')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/FBI/Castle.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no") 

                self.mainloop()

def DPulse():
        Pulse()

class Pulse(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Pulse')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/FBI/Pulse.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DDoc():
        Doc()

class Doc(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Doc')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GIGN/Doc.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DRook():
        Rook()

class Rook(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Rook')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GIGN/Rook.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DJager():
        Jager()

class Jager(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Jager')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GSG/Jager.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DBandit():
        Bandit()

class Bandit(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Bandit')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/GSG/Bandit.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DKapkan():
        Kapkan()

class Kapkan(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Kapkan')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/Spetsnaz/Kapkan.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()

def DTachanka():
        Tachanka()

class Tachanka(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Tachanka')
                self.geometry('900x800')

                img = ImageTk.PhotoImage(Image.open("Images/Images/Informations/Operators/Spetsnaz/Tachanka.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                self.mainloop()                       
