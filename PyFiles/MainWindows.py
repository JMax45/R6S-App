import sys
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os
from PyFiles.Seasons import *
from PyFiles.Operators import *
from PyFiles.Operators import *
from PyFiles.RandWindow import *
from PyFiles.Definitions import *
from PyFiles.OperatorsElite import *
           
def CInfo():
    window2 = Toplevel()             #
    window2.title('Contatti')        #  Configurazione della finestra
    window2.geometry('700x150')      #
    window2.iconbitmap(default='Images/Icons/Icon.ico')

    img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background8.jpg"))           #  
    panel = Label(window2, image = img)                                               #  Immagine di sfondo    
    panel.pack(side = "bottom", fill = "both", expand = "no")

    Label(window2, text='Questo programma è stato creato da JMax e dal suo assistente,').place(y = 15, x = 180)
    Label(window2, text='se volete contattarmi per qualche spiegazione mandatemi una mail: tachanka.tachankin@mail.ru,').place(y = 40, x = 90)
    Label(window2, text='inoltre se volete guardare i miei video sul mio canale youtube').place(y = 65, x = 183)
    
    Link1 = Label(window2, text="JMax", fg="blue", cursor="hand2")           
    Link1.place(y = 90, x = 325)                                                             
    Link1.bind("<Button-1>", callback3)
    
    Label(window2, text=' e per giocare con me alla PS4 il mio ID è il seguente: maksgensta').place(y = 115, x = 176)

    window2.mainloop()

class Stagioni(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Stagioni')
                self.geometry('700x500')
                tk.Label(self, text='Scegli la stagione').pack()

                self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background2.jpg"))
                self.panel = Label(self, image =self.img)
                self.panel.pack(side = "bottom", fill = "both", expand = "no")

                Button(self, text='Chimera', command= DChimera).place(y = 100, x = 10)

                Button(self, text='White Noise', command= DWhiteNoise).place(y = 190, x = 10)
                Button(self, text='Blood Orchid', command = DBloodOrchid).place(y = 190, x = 88)
                Button(self, text='Operation Health', command = DOperationHealth).place(y = 190, x = 173)
                Button(self, text='Velvet Shell', command = DVelvetShell).place(y = 190, x = 278 )

                Button(self, text='Red Crow', command= DRedCrow).place(y = 280, x = 10)
                Button(self, text='Skull Rain', command = DSkullRain).place(y = 280, x = 75)
                Button(self, text='Dust Line', command = DDustLine).place(y = 280, x = 140)
                Button(self, text='Black Ice', command = DBlackIce).place(y = 280, x = 203)

                self.mainloop()

class Operatori(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Operatori')
                self.geometry('700x500')

                img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background3.jpg"))           
                panel = Label(self, image = img)                                                  
                panel.pack(side = "bottom", fill = "both", expand = "no")

                #Gli Attaccanti
                Button(self, text='Lyon', command= DLyon).place(y = 130, x = 18)
                Button(self, text='Finka', command= DFinka).place(y = 130, x = 60)
                Button(self, text='Dokkaebi', command= DDokkaebi).place(y = 130, x = 145 )
                Button(self, text='Zofia', command= DZofia).place(y = 130, x = 103 )
                Button(self, text='Ying', command= DYing).place(y = 130, x = 209)
                Button(self, text='Jackal', command= DJackal).place(y = 130, x = 248)
                Button(self, text='Hibana', command= DHibana).place(y = 130, x = 294)
                Button(self, text='Capitao', command= DCapitao).place(y = 130, x = 347)
                Button(self, text='Blackbeard', command= DBlackbeard).place(y = 130, x = 403)
                Button(self, text='Buck', command= DBuck).place(y = 130, x = 476)
                
                Button(self, text='Sledge', command= DSledge).place(y = 160, x = 18)
                Button(self, text='Ash', command= DAsh).place(y = 160, x = 68)
                Button(self, text='Thermite', command= DThermite).place(y = 160, x = 103)
                Button(self, text='Twitch', command= DTwitch).place(y = 160, x = 166)
                Button(self, text='Montagne', command= DMontagne).place(y = 160, x = 217)
                Button(self, text='Blitz', command= DBlitz).place(y = 160, x = 287)
                Button(self, text='IQ', command= DIQ).place(y = 160, x = 324)
                Button(self, text='Fuze', command= DFuze).place(y = 160, x = 352)
                Button(self, text='Glaz', command= DGlaz).place(y = 160, x = 391)

                #I Difensori
                Button(self, text='Vigil', command= DVigil).place(y = 332, x = 18)
                Button(self, text='Ela', command= DEla).place(y = 332, x = 56)
                Button(self, text='Mira', command= DMira).place(y = 332, x = 86)
                Button(self, text='Lesion', command= DLesion).place(y = 332, x = 126)
                Button(self, text='Echo', command= DEcho).place(y = 332, x = 176)
                Button(self, text='Caveira', command= DCaveira).place(y = 332, x = 218)
                Button(self, text='Valkyrie', command= DValkyrie).place(y = 332, x = 273)
                Button(self, text='Frost', command= DFrost).place(y = 332, x = 329)

                Button(self, text='Mute', command= DMute).place(y = 362, x = 18)
                Button(self, text='Smoke', command= DSmoke).place(y = 362, x = 61)
                Button(self, text='Castle', command= DCastle).place(y = 362, x = 113)
                Button(self, text='Pulse', command= DPulse).place(y = 362, x = 161)
                Button(self, text='Doc', command= DDoc).place(y = 362, x = 205)
                Button(self, text='Rook', command= DRook).place(y = 362, x = 242)
                Button(self, text='Jager', command= DJager).place(y = 362, x = 285)
                Button(self, text='Bandit', command= DBandit).place(y = 362, x = 328)
                Button(self, text='Kapkan', command= DKapkan).place(y = 362, x = 378)
                Button(self, text='Tachanka', command= DTachanka).place(y = 362, x = 433)

                self.mainloop()

def Soundtrack1():
        os.startfile('Sounds\\Soundtrack\\Ben Frost - Deadzone.mp3')
def Soundtrack2():
        os.startfile('Sounds\\Soundtrack\\Ben Frost - First Strike.mp3')
def Soundtrack3():
        os.startfile('Sounds\\Soundtrack\\Paul Haslinger - Purple Heart.mp3')             
def Soundtrack4():
        os.startfile('Sounds\\Soundtrack\\Paul Haslinger - Reactivate Team Rainbow.mp3')
def Soundtrack5():
        os.startfile('Sounds\\Soundtrack\\Paul Haslinger and Ben Frost - The Brief.mp3')    

class Soundtrack(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Soundtrack')
                self.geometry('700x500')

                self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background9.jpg"))
                self.panel = Label(self, image =self.img)
                self.panel.pack(side = "bottom", fill = "both", expand = "no")

                Button(self, text='PLAY', font='Times 16', command=Soundtrack1).place(y = 152, x = 40)
                Button(self, text='PLAY', font='Times 16', command=Soundtrack2).place(y = 218, x = 40)
                Button(self, text='PLAY', font='Times 16', command=Soundtrack3).place(y = 281, x = 40)
                Button(self, text='PLAY', font='Times 16', command=Soundtrack4).place(y = 345, x = 40)
                Button(self, text='PLAY', font='Times 16', command=Soundtrack5).place(y = 411, x = 40)

                self.iconbitmap(default='Images/Icons/Icon.ico')
                self.mainloop()

class Randomizer1(tk.Toplevel):
        def __init__(self):
            super().__init__()
            self.init_child()  

        def init_child(self):

            
                def coloriS1():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS2():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec2.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS3():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec3.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS4():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec4.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS5():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec5.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS6():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec6.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS7():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec7.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS8():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec8.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS9():
                        self.panel.destroy()
                        self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec9.jpg"))
                        self.panel = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                def coloriS10():
                        self.img.config = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Special/WallSpec10.jpg"))
                        self.panel.config = Label(self, image =self.img)
                        self.panel.pack(side = "bottom", fill = "both", expand = "no")
                      
                

                self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Randomizer2.jpg"))
                self.panel = Label(self, image =self.img)
                self.panel.pack(side = "bottom", fill = "both", expand = "no")



                def mnotte():
                        self["bg"] = "black"
                        self.panel.destroy()
                def mgiorno():
                        self["bg"] = "white"
                        self.panel.destroy()

                def colori():
                        self["bg"] = "green"
                        self.panel.destroy()
                def colori2():
                        self["bg"] = "blue"
                        self.panel.destroy()
                def colori3():
                        self["bg"] = "red"
                        self.panel.destroy()
                def colori4():
                        self["bg"] = "yellow"
                        self.panel.destroy()
                def colori5():
                        self["bg"] = "purple"
                        self.panel.destroy()
                def colori6():
                        self["bg"] = "pink"
                        self.panel.destroy()
                def colori7():
                        self["bg"] = "brown"
                        self.panel.destroy()
                def colori8():
                        self["bg"] = "grey"
                        self.panel.destroy()
                def colori9():
                        self["bg"] = "orange"
                        self.panel.destroy() 

                        

                m = Menu(self)
                submenu = Menu(self)
                submenu2 = Menu(self)
                context_menu = Menu(self)                                         #
                self.config(menu=m)                                               #
                fn = Menu(m, tearoff=0)
                fn1 = Menu(m, tearoff=0)
                fn2 = Menu(m, tearoff=0)
        
                m.add_cascade(label='Personalizza', menu=fn1)
                fn1.add_command(label="Modalita' notte", command=mnotte)
                fn1.add_command(label="Modalita' giorno", command=mgiorno)
                fn1.add_separator()
                fn1.add_cascade(label='Sfondi', menu=submenu)
                fn1.add_cascade(label='Sfondi Speciali', menu=submenu2)
                
                m.add_cascade(label='Opzioni', menu=fn2)
                fn2.add_command(label='Pronostico', command=wpronostico)
                fn2.add_command(label='Spawn', command=spawn)
                fn2.add_command(label='Mirino', command=mirino)

                m.add_cascade(label='Info', menu=fn)
                fn.add_command(label='Contatti', command=CInfo)
                fm = Menu(m, tearoff=0)                                           #
                self.config(menu=m)

                submenu.add_command(label="Verde", command=colori)
                submenu.add_command(label="Blu", command=colori2)
                submenu.add_command(label="Rosso", command=colori3)
                submenu.add_command(label="Giallo", command=colori4)
                submenu.add_command(label="Viola", command=colori5)
                submenu.add_command(label="Rosa", command=colori6)
                submenu.add_command(label="Marrone", command=colori7)
                submenu.add_command(label="Grigio", command=colori8)
                submenu.add_command(label="Arancione", command=colori9)

                submenu2.add_command(label="Verde", command=coloriS1)
                submenu2.add_command(label="Lime", command=coloriS2)
                submenu2.add_command(label="Lucciola", command=coloriS3)
                submenu2.add_command(label="Zepardo", command=coloriS4)
                submenu2.add_command(label="Mandarino", command=coloriS5)
                submenu2.add_command(label="Chano", command=coloriS6)
                submenu2.add_command(label="Brillantini", command=coloriS7)
                submenu2.add_command(label="Bordeaux", command=coloriS8)
                submenu2.add_command(label="Mela", command=coloriS9)
                submenu2.add_command(label="Fucsia", command=coloriS10)

                self.title('R6S App | Randomizer')
                self.geometry('450x450+500+300')
                self.iconbitmap(default='Images/Icons/Icon.ico')

                def DAttaccanti():
                    self.image = ImageTk.PhotoImage(Image.open(random.choice(code_list6)))
                    tk.Label(self, image=self.image).place(y = 40, x = 150)

                def DDifensori():
                    self.image = ImageTk.PhotoImage(Image.open(random.choice(code_list7)))
                    tk.Label(self, image=self.image).place(y = 40, x = 150)  

                ButtonD = Button(self, text= 'Difesa', fg='Black',bg='orange', command=DDifensori).place(x = 115, y = 5,
                                                                                                         width = 70)
                ButtonF = Button(self, text='Attacco', fg='Black',bg='orange', command=DAttaccanti).place(x = 250, y = 5,
                                                                                                          width = 70)

                self.mainloop()

class DEliteS(tk.Toplevel):
        def __init__(self):
                super().__init__()
                self.init_child()

        def init_child(self):
                self.title('Schermate Elite')
                self.geometry('600x400')

                self.img = ImageTk.PhotoImage(Image.open("Images/Backgrounds/Background10.jpg"))
                self.panel = Label(self, image =self.img)
                self.panel.pack(side = "bottom", fill = "both", expand = "no")

                Button(self, text='Thermite', command= DThermiteElite).place(x = 8, y = 145)
                Button(self, text='Sledge', command= DSledgeElite).place(x = 71, y = 145)
                Button(self, text='Blackbeard', command= DBlackbeardElite).place(x = 121, y = 145)
                Button(self, text='Fuze', command= DFuzeElite).place(x = 194, y = 145)
                Button(self, text='Twitch', command= DTwitchElite).place(x = 233, y = 145)
                Button(self, text='IQ', command= DIQElite).place(x = 285, y = 145)

                Button(self, text='Mute', command= DMuteElite).place(x = 8, y = 273)
                Button(self, text='Pulse', command= DPulseElite).place(x = 52, y = 273)
                Button(self, text='Rook', command= DRookElite).place(x = 96, y = 273)
                Button(self, text='Kapkan', command= DKapkanElite).place(x = 139, y = 273)
                Button(self, text='Jager', command= DJagerElite).place(x = 194, y = 273)
                
                self.iconbitmap(default='Images/Icons/Icon.ico')
                
                self.mainloop()              
                
