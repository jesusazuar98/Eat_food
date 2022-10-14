from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import datetime

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

        #Se añaden las imagenes para que se queden puestas
        self.images=[]

        self.icons_views={'images/home.png':lambda:self.home_view(),'images/user.png':lambda:self.user_view(),'images/milk.png':lambda:self.food_view()}

        for i,x in self.icons_views.items():
            
            self.icono=Frame(self.frame_panel,bg='#C6DCCF',bd=1,relief='solid',width=self.redimension(self.x_y[0],20),height=self.redimension(self.x_y[1],34))
            self.icono.pack(side='top')
            self.boton_image(self.icono,i,0,0,1,1,bg='#C6DCCF',comand=x)


        self.posi=0

        self.home_view()




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
    def boton_image(self,myframe,i_image,x,y,rw,rh,comand,bg='white'):
        self.myimage=PhotoImage(file=i_image)
        self.images.append(self.myimage)
        
        self.image=Button(myframe,image=self.myimage,bg=bg,command=comand)
        self.image.place(x=x,y=y,relwidth=rw,relheight=rh)


    #Añadir una imagen
    def add_image(self,myframe,i_image,x,y,rw,rh,bg='white'):

        self.myimage=PhotoImage(file=i_image)

        self.image=Label(myframe,image=self.myimage,bg=bg)
        self.image.place(x=x,y=y,relwidth=rw,relheight=rh)







    #Vista del home
    def home_view(self,date=datetime.datetime.today()):

        if self.posi!=0:
            self.frame_principal.destroy()

        self.posi+= 1
        self.frame_principal = Frame(self.panel,bg='#DBDBDB',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both',expand=True)


        
        Label(self.frame_principal,text='Tu registro de comidas:',bg="#DBDBDB",font=('Arial',12)).place(relx=0.01,rely=0.1)

        self.boton1=Button(self.frame_principal,font=('Arial',10),text='<',command=lambda:self.cambio_fecha('<',date))
        self.boton1.place(relx=0.25,rely=0.1)

        self.fecha=Label(self.frame_principal,text=date.strftime('%d/%m/%Y'),font=('Arial',12))
        self.fecha.place(relx=0.28,rely=0.1)

        self.boton2=Button(self.frame_principal,font=('Arial',10),text='>',command=lambda:self.cambio_fecha('>',date))
        self.boton2.place(relx=0.39,rely=0.1)
        
        try:
            self.resumen_diario()
        
            Label(self.frame_principal,text="Calorías",bg="#C6DCCF",font=('Arial',12)).place(relx=0.2,rely=0.3)
            Label(self.frame_principal,text="Proteinas",bg="#C6DCCF",font=('Arial',12)).place(relx=0.3,rely=0.3)
            Label(self.frame_principal,text="Grasas",bg="#C6DCCF",font=('Arial',12)).place(relx=0.4,rely=0.3)
            Label(self.frame_principal,text="Carbo\nhidratos",bg="#C6DCCF",font=('Arial',12)).place(relx=0.5,rely=0.3)
            Label(self.frame_principal,text="Azucar",bg="#C6DCCF",font=('Arial',12)).place(relx=0.6,rely=0.3)



            Label(self.frame_principal,text="Desayuno",bg="#DBDBDB",font=('Arial',12)).place(relx=0.01,rely=0.4)
            Label(self.frame_principal,text="Almuerzo",bg="#DBDBDB",font=('Arial',12)).place(relx=0.01,rely=0.5)
            Label(self.frame_principal,text="Comida",bg="#DBDBDB",font=('Arial',12)).place(relx=0.01,rely=0.6)
            Label(self.frame_principal,text="Cena",bg="#DBDBDB",font=('Arial',12)).place(relx=0.01,rely=0.7)

            add_food=Button(self.frame_principal,font=('Arial',10),text='Añadir comida',command=lambda:self.view_add_food(date.strftime('%Y/%m/%d')))
            add_food.place(relx=0.4,rely=0.8)
        
        except:

            Label(self.frame_principal,text="Ha ocurrido un error en la base de datos",bg="#DBDBDB",font=('Arial',30)).place(relx=0.01,rely=0.5)



    #Cambio de fecha
    def cambio_fecha(self,ope,fecha):

        if ope=='<':

            fecha=fecha-datetime.timedelta(days=1)

            self.home_view(date=fecha)

        if ope=='>':

            fecha=fecha+datetime.timedelta(days=1)

            self.home_view(date=fecha)
    
    def add_food(self,date,alimento,cantidad):
        
        data=Database()

        alimento=data.producto(alimento)
        id=data.id_user(self.usu)
        
        valores=[(i*cantidad)/100 for i in alimento[3:]]
        valores.append(id)
        valores.append(alimento[0])
        print(valores)


    def view_add_food(self,date):
        
        self.frame_principal.destroy()
        self.frame_principal = Frame(self.panel,bg='#DBDBDB',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both',expand=True)

        lista=Listbox(self.frame_principal,selectmode=SINGLE,widt=30,font=('Arial',10))
        lista.place(x=self.redimension(self.x_y[0],4),y=self.redimension(self.x_y[1],25))


        self.food=Entry(self.frame_principal,font=('Arial',10),width=30)
        self.food.place(x=self.redimension(self.x_y[0],4),y=self.redimension(self.x_y[1],10))

        self.search=Button(self.frame_principal,font=('Arial',10),text='Buscar alimento',command=lambda:self.search_food(self.food.get(),lista))
        self.search.place(x=self.redimension(self.x_y[0],10),y=self.redimension(self.x_y[1],15))

        self.enviar=Button(self.frame_principal,font=('Arial',10),text='Añadir',command=lambda:self.add_food(date,lista.get(lista.curselection()[0]),50))
        self.enviar.place(x=self.redimension(self.x_y[0],10),y=self.redimension(self.x_y[1],80))







    def resumen_diario(self):

        pass










    #Vista usuarios
    def user_view(self):

        self.frame_principal.destroy()
        self.frame_principal = Frame(self.panel,bg='#DBDBDB',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both',expand=True)
        
        Label(self.frame_principal,text='MI PERFIL',bg="#DBDBDB",font=('Arial',16)).place(x=self.redimension(self.x_y[0],35),y=self.redimension(self.x_y[1],10))

        data=self.data_user()

        Label(self.frame_principal,text='Nombre de usuario: ',bg="#DBDBDB",font=('Arial',12)).place(x=self.redimension(self.x_y[0],5),y=self.redimension(self.x_y[1],20))
        self.name_user=Label(self.frame_principal,text=data[0],bg="#DBDBDB",font=('Arial',12,'bold'))
        self.name_user.place(x=self.redimension(self.x_y[0],20),y=self.redimension(self.x_y[1],20))


        Label(self.frame_principal,text='Estatura: ',bg="#DBDBDB",font=('Arial',12)).place(x=self.redimension(self.x_y[0],5),y=self.redimension(self.x_y[1],25))
        self.tall=Label(self.frame_principal,text=str(data[1])+'cm',bg="#DBDBDB",font=('Arial',12,'bold'))
        self.tall.place(x=self.redimension(self.x_y[0],12),y=self.redimension(self.x_y[1],25))


        Label(self.frame_principal,text='Peso: ',bg="#DBDBDB",font=('Arial',12)).place(x=self.redimension(self.x_y[0],5),y=self.redimension(self.x_y[1],30))
        self.weigth=Label(self.frame_principal,text=str(data[2])+'k',bg="#DBDBDB",font=('Arial',12,'bold'))
        self.weigth.place(x=self.redimension(self.x_y[0],12),y=self.redimension(self.x_y[1],30))


        Label(self.frame_principal,text='Cambiar estatura: ',bg="#DBDBDB",font=('Arial',12)).place(x=self.redimension(self.x_y[0],5),y=self.redimension(self.x_y[1],40))
        self.change_tall=Entry(self.frame_principal,font=('Arial',10),width=10)
        self.change_tall.place(x=self.redimension(self.x_y[0],18),y=self.redimension(self.x_y[1],40))

        Label(self.frame_principal,text='Cambiar peso: ',bg="#DBDBDB",font=('Arial',12)).place(x=self.redimension(self.x_y[0],5),y=self.redimension(self.x_y[1],45))
        self.change_weigth=Entry(self.frame_principal,font=('Arial',10),width=10)
        self.change_weigth.place(x=self.redimension(self.x_y[0],18),y=self.redimension(self.x_y[1],45))
        
        self.search=Button(self.frame_principal,font=('Arial',10),text='Cambiar',command=lambda:self.change_profile(data[0],self.change_tall.get(),self.change_weigth.get()))
        self.search.place(x=self.redimension(self.x_y[0],10),y=self.redimension(self.x_y[1],50))


    #Cambiar datos del perfil
    def change_profile(self,user,altura,peso):
        
        self.data=Database()



        if peso=='' and altura=='':
        
            messagebox.showinfo(message='Introduce algun valor para cambiar.')


        elif altura=='':
            peso=round(float(peso),2)
            
            self.data.change_weigth(user,peso)

            self.user_view()

        elif peso=='':
            
            self.data.change_tall(user,altura)

            self.user_view()
        
        else:
            self.data.change_weigth(user,peso)
            self.data.change_tall(user,altura)
            self.user_view()

    #Datos del usuario
    def data_user(self):
        
        self.data=Database()

        return self.data.user_data(self.usu)









    #Metodos vista comida
    def food_view(self):
        self.frame_principal.destroy()
        self.frame_principal = Frame(self.panel,bg='#DBDBDB',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both',expand=True)

        self.list=Listbox(self.frame_principal,selectmode=SINGLE,widt=30,font=('Arial',10))
        self.list.place(x=self.redimension(self.x_y[0],4),y=self.redimension(self.x_y[1],25))

        self.seleccionar=Button(self.frame_principal,font=('Arial',10),text='Seleccionar',command=lambda:self.seleccion_item())
        self.seleccionar.place(x=self.redimension(self.x_y[0],26),y=self.redimension(self.x_y[1],35))


        self.food=Entry(self.frame_principal,font=('Arial',10),width=30)
        self.food.place(x=self.redimension(self.x_y[0],4),y=self.redimension(self.x_y[1],10))
        
        self.search=Button(self.frame_principal,font=('Arial',10),text='Buscar alimento',command=lambda:self.search_food(self.food.get(),self.list))
        self.search.place(x=self.redimension(self.x_y[0],10),y=self.redimension(self.x_y[1],15))

        self.info_nutri=Text(self.frame_principal,bg='white',width=40,height=11)
        self.info_nutri.place(x=self.redimension(self.x_y[0],40),y=self.redimension(self.x_y[1],25))


    #Buscar alimentos
    def search_food(self,input,list):

        data=Database()

        productos=data.food(input)
        

        for i in range(len(productos)):
            list.insert(i,productos[i])


    #Datos del alimento seleccionado de la lista
    def seleccion_item(self):
        try:
            posi=self.list.curselection()[0]

            data=Database()
            
            valores_nutricionales=data.producto(self.list.get(posi))

            text=f"""{valores_nutricionales[1].upper()}

Info. Nutricional
Tamaño de la porcion: {valores_nutricionales[2]}g
Energía: {valores_nutricionales[3]} Kcal
Grasas: {valores_nutricionales[4]}g
Grasas saturadas: {valores_nutricionales[5]}g
Carbohidratos: {valores_nutricionales[6]}g
Azucar: {valores_nutricionales[7]}g
Proteina: {valores_nutricionales[8]}g
Sal: {valores_nutricionales[9]}g
    """
            self.info_nutri.delete('1.0',END)
            self.info_nutri.insert(INSERT,text)

        except:
            messagebox.showinfo(message='Porfavor seleccione un alimento de la lista.')






