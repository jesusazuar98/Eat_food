from tkinter import *
from tkinter import messagebox
from database import Database


class Sign_in:


    def __init__(self):


        self.raiz=Tk()

        self.center_window()
        self.raiz.title('Eat food')
        self.raiz.iconbitmap('images/icono.ico')
        self.raiz.resizable(width=0,height=0)
        
        self.frame=Frame(width=1000,height=600)
        self.frame.pack()

        Label(self.frame,text='Creación de cuenta',font=('Arial',24),fg="grey",pady=50).pack(fill='both')
        Label(self.frame,text='Nombre de usuario',font=('Arial',16),fg="grey").pack()
        self.user=Entry(self.frame,font=('Arial',16))
        self.user.pack(fill='x',padx=20,pady=10)

        Label(self.frame,text='Contraseña',font=('Arial',16),fg="grey").pack(fill='both')
        self.password=Entry(self.frame,font=('Arial',16))
        self.password.pack(fill='x',padx=20,pady=10)
        self.password.config(show='*')

        Label(self.frame,text='Vuelve a introducir la contraseña',font=('Arial',16),fg="grey").pack(fill='both')
        self.password2=Entry(self.frame,font=('Arial',16))
        self.password2.pack(fill='x',padx=20,pady=10)
        self.password2.config(show='*')

        self.inicio=Button(self.frame,text='Crear cuenta',font=('Arial',18),bg='#C6DCCF',command=lambda:self.create_account())
        self.inicio.pack(padx=20,pady=20)



        self.raiz.mainloop()


    #Centrar ventana
    def center_window(self,ancho=1000,largo=600):
        self.screen_x=self.raiz.winfo_screenwidth()
        self.screen_y=self.raiz.winfo_screenheight()
        x=int((self.screen_x/2)-(ancho/2))
        y=int((self.screen_y/2)-(largo/2))

        self.raiz.geometry(f'{ancho}x{largo}+{x}+{y}')



    def create_account(self):

        self.data=Database()

        if len(self.user.get())<5:
            messagebox.showinfo(message='El nombre de usuario debe ser mas largo.')
        
        if len(self.password.get())<5:
            messagebox.showinfo(message='La contraseña debe ser mas larga.')

        else:
            self.com=self.data.comprobar_usuario(self.user.get(),self.password.get(),self.password2.get())

            if self.com==0:
                messagebox.showinfo(message='El nombre de usuario ya existe intentelo con uno nuevo')
                self.user.delete(0,END)
                self.password.delete(0,END)
                self.password2.delete(0,END)


            if self.com==1:
                messagebox.showinfo(message='La contraseña introducida no es la misma, intentelo de nuevo.')
                self.user.delete(0,END)
                self.password.delete(0,END)
                self.password2.delete(0,END)

            if self.com==2:
                
                self.data.crear_usuario(self.user.get(),self.password.get())

                messagebox.showinfo(message='La cuenta se ha creado correctamente ya puede iniciar sesion.')
                
                self.raiz.destroy()


