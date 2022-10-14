import sqlite3
import hashlib


class Database:

    def __init__(self):

        self.con=sqlite3.connect('eat_food.db')
        self.cursor=self.con.cursor()

    #Creacion e inicio de sesion
    def inicio_session(self,user,pass1):
        password=hashlib.sha256(pass1.encode('utf-8')).hexdigest()

        sql=f"SELECT COUNT(Name_user) FROM users WHERE Name_user =(?) AND Pass=(?)"

        self.cursor.execute(sql,(user,password))

        return self.cursor.fetchone()[0]
    
    #Comprobacion de si existe un usuario con ese nombre y si la contraseña es correcta en la comprobacion
    def comprobar_usuario(self,user,pass1,pass2):


        sql =f"SELECT COUNT(Name_user) FROM users WHERE Name_user='{user}'"

        self.cursor.execute(sql)


        num=self.cursor.fetchone()[0]

        if num!=0:
            

            return 0

        if pass1!=pass2:
            

            return 1

        if num==0 and pass1==pass2:
            

            return 2

    
    #Creacion del usuario
    def crear_usuario(self,user,pass1):

        password=hashlib.sha256(pass1.encode('utf-8')).hexdigest()

        sql=f"INSERT INTO users (Name_user,Pass) VALUES (?,?)"
        self.cursor.execute(sql,(user,password))


        self.con.commit()
        self.con.close()


    #Cambiar el peso
    def change_weigth(self,user,peso):

        sql=f"UPDATE users SET Weight={peso} WHERE Name_user='{user}'"

        self.cursor.execute(sql)
        self.con.commit()
        

    #Cambiar el tamaño
    def change_tall(self,user,tall):

        sql=f"UPDATE users SET Tall_user={tall} WHERE Name_user='{user}'"

        self.cursor.execute(sql)
        self.con.commit()
        


    def user_data(self,user):

        sql=f"SELECT * FROM users WHERE Name_user='{user}'"

        self.cursor.execute(sql)

        data=self.cursor.fetchone()[1:]

        self.con.close()

        data=["0" if i==None else i for i in data]
        del data[1]

        

        return data

    def id_user(self,user):

        sql=f"SELECT * FROM users WHERE Name_user='{user}'"

        self.cursor.execute(sql)

        data=self.cursor.fetchone()[0]

        self.con.close()

        return data



    #Alimentos

    def food(self,name):

        self.cursor.execute(f"SELECT Name FROM alimentos WHERE Name LIKE '%{name}%' LIMIT 10")

        alimentos=self.cursor.fetchall()


        alimentos=[i[0] for i in alimentos]

        self.con.close()

        return alimentos


    def producto(self,name):

        self.cursor.execute(f"SELECT * FROM alimentos WHERE Name='{name}'")

        return self.cursor.fetchone()


    def añadir_comida(self,date,moment):
        
        pass




# con=sqlite3.connect('eat_food.db')

# cursor=con.cursor()

# sql="UPDATE alimentos SET Name=Name || '(hacendado)'"

# cursor.execute(sql)

# sql2="SELECT * FROM alimentos"

# cursor.execute(sql2)
# print(cursor.fetchone())

# con.commit()
# con.close()
