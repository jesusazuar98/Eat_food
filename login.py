from cgitb import text
from tkinter import *
from main_panel import Panel
from sing_in import Sign_in

#Creamos la clase grafic

class Login:


    def verificar(self):

        self.usu=self.user.get().replace(' ','')
        self.pas=self.password.get().replace(' ','')



        #if self.usu=='root' and self.pas=='root':

        self.raiz.destroy()

        self.panel=Panel(self.usu,self.pas)


    #Metemos la raiz en el constructor
    def __init__(self):

        self.raiz=Tk()

        #Frame del logo
        self.frame_logo=Frame(self.raiz,relief=SOLID,bd=0,width=300,padx=10,pady=10,bg='#C6DCCF')
        self.frame_logo.pack(side="left",fill='both',expand=False)


        #Frame inicio
        self.frame_inicio=Frame(self.raiz,relief=SOLID,bg='#fcfcfc')
        self.frame_inicio.pack(side="right",fill='both',expand=True)


        #Frame top
        self.frame_top=Frame(self.frame_inicio,height=50,bd=0,bg='black')
        self.frame_top.pack(side='top',fill='x')


        #Frame fill
        
        self.frame_fill=Frame(self.frame_inicio,height=50,bd=0,bg='white')
        self.frame_fill.pack(side='bottom',expand=True,fill='both')


        self.center_window()
        self.title_dimession()

        #Logo
        self.add_image(self.frame_logo,'images/logo.png',0,0,1,1,bg='#C6DCCF')

        #Zona inicio de sesion

        Label(self.frame_top,text='Inicio de sesion',font=('Arial',24),fg="grey",bg='#fcfcfc',pady=50).pack(expand=True,fill='both')
        Label(self.frame_fill,text='Usuario',font=('Arial',16),fg="grey",bg='#fcfcfc',anchor='w').pack(fill='x',pady=10,padx=10)
        self.user=Entry(self.frame_fill,font=('Arial',16))
        self.user.pack(fill='x',padx=20,pady=10)

        Label(self.frame_fill,text='Contraseña',font=('Arial',16),fg="grey",bg='#fcfcfc',anchor='w').pack(fill='x',pady=10,padx=10)
        self.password=Entry(self.frame_fill,font=('Arial',16))
        self.password.pack(fill='x',padx=20)
        self.password.config(show='*')

        self.inicio=Button(self.frame_fill,text='Iniciar sesion',font=('Arial',18),bg='#C6DCCF',command=lambda:self.verificar())
        self.inicio.pack(padx=20,side='left')

        self.inicio=Button(self.frame_fill,text='Crear cuenta',font=('Arial',18),bg='#C6DCCF',command=lambda:self.crear_cuenta())
        self.inicio.pack(padx=20,side='right')
        

        self.raiz.mainloop()



    #Centrar ventana
    def center_window(self,ancho=1000,largo=600):
        self.screen_x=self.raiz.winfo_screenwidth()
        self.screen_y=self.raiz.winfo_screenheight()
        x=int((self.screen_x/2)-(ancho/2))
        y=int((self.screen_y/2)-(largo/2))

        self.raiz.geometry(f'{ancho}x{largo}+{x}+{y}')


    #Añade las dimensiones de la ventana, titulo, icono y color de fondo
    def title_dimession(self):
        self.raiz.config(bg='#fcfcfc')
        self.raiz.resizable(width=0,height=0)


        self.raiz.title('Eat food')
        self.raiz.iconbitmap('images/icono.ico')


    def crear_cuenta(self):

        self.raiz.destroy()

        self.sign_in=Sign_in()

        self.log=Login()





    #Añadir una imagen
    def add_image(self,myframe,i_image,x,y,rw,rh,bg='white'):

        self.myimage=PhotoImage(file=i_image)

        Label(myframe,image=self.myimage,bg=bg).place(x=x,y=y,relwidth=rw,relheight=rh)




