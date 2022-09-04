from tkinter import *
from database import Database

class Panel:


    def __init__(self,usu,password):
        
        self.usu = usu
        self.password = password

        self.panel=Tk()

        self.center_window()

        self.data=Database()

        self.data.all_food()


        self.panel.mainloop()


    def center_window(self,ancho=1000,largo=600):
        self.screen_x=self.panel.winfo_screenwidth()
        self.screen_y=self.panel.winfo_screenheight()
        x=int((self.screen_x/2)-(ancho/2))
        y=int((self.screen_y/2)-(largo/2))

        self.panel.geometry(f'{ancho}x{largo}+{x}+{y}')