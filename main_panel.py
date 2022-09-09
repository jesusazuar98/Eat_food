from tkinter import *
from database import Database

class Panel:


    def __init__(self,usu,password):
        
        self.usu = usu
        self.password = password

        self.panel=Tk()
        self.x_y=self.center_window()
        self.panel.title('Eat food')
        self.panel.iconbitmap('images/icono.ico')
        self.panel.resizable(width=0,height=0)

        #Frame panel izquierdo
        

        self.frame_panel = Frame(self.panel,bg='white',width=self.redimension(self.x_y[0],20),height=self.x_y[1])
        self.frame_panel.pack(side='left',fill='both')

        self.images =[]

        self.icons =['images/home.png','images/user.png','images/milk.png']

        for i in range(len(self.icons)):

            self.icono=Frame(self.frame_panel,bg='#C6DCCF',bd=1,relief='solid',width=self.redimension(self.x_y[0],20),height=self.redimension(self.x_y[1],34))
            self.icono.pack(side='top')
            self.boton_image(self.icono,self.icons[i],0,0,1,1,bg='#C6DCCF')












        #Frame panel principal
        self.frame_principal = Frame(self.panel,bg='#B3B0B0',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both')




        self.panel.mainloop()

    #Centrar ventana
    def center_window(self,ancho=1000,largo=600):
        self.screen_x=self.panel.winfo_screenwidth()
        self.screen_y=self.panel.winfo_screenheight()
        x=int((self.screen_x/2)-(ancho/2))
        y=int((self.screen_y/2)-(largo/2))

        self.panel.geometry(f'{ancho}x{largo}+{x}+{y}')
        
        return [ancho,largo]


    #Redimensionar
    def redimension(self,eje,porcentaje):


        operacion=(eje*porcentaje)/100
        
        
        return int(operacion)

    #Añadir un boton con una imagen
    def boton_image(self,myframe,i_image,x,y,rw,rh,bg='white'):
        self.myimage=PhotoImage(file=i_image)
        self.images.append(self.myimage)
        
        self.image=Button(myframe,image=self.myimage,bg=bg)
        self.image.place(x=x,y=y,relwidth=rw,relheight=rh)


    #Añadir una imagen
    def add_image(self,myframe,i_image,x,y,rw,rh,bg='white'):

        self.myimage=PhotoImage(file=i_image)

        self.image=Label(myframe,image=self.myimage,bg=bg)
        self.image.place(x=x,y=y,relwidth=rw,relheight=rh)
