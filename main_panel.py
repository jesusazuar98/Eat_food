from tkinter import *
from tkinter import messagebox

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


    def home_view(self):

        if self.posi!=0:
            self.frame_principal.destroy()

        self.posi+= 1
        self.frame_principal = Frame(self.panel,bg='#DBDBDB',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both',expand=True)
        
        Label(self.frame_principal,text='Hello guys!',bg="#DBDBDB").place(x=self.redimension(self.x_y[0],0.5),y=self.redimension(self.x_y[1],10))


    def user_view(self):

        self.frame_principal.destroy()
        self.frame_principal = Frame(self.panel,bg='#DBDBDB',width=self.redimension(self.x_y[0],80),height=self.x_y[1])
        self.frame_principal.pack(side='left',fill='both',expand=True)
        
        Label(self.frame_principal,text='Hello user!',bg="#DBDBDB").place(x=self.redimension(self.x_y[0],0.5),y=self.redimension(self.x_y[1],10))















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

        self.info_nutri=Text(self.frame_principal,bg='white',width=40)
        self.info_nutri.place(x=self.redimension(self.x_y[0],40),y=self.redimension(self.x_y[1],15))


    def search_food(self,input,list):

        self.data=Database()

        productos=self.data.food(input)
        

        for i in range(len(productos)):
            list.insert(i,productos[i])

    def seleccion_item(self):
        try:
            posi=self.list.curselection()[0]

            self.data=Database()
            
            valores_nutricionales=self.data.producto(self.list.get(posi))

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






