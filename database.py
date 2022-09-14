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
    
    def comprobar_usuario(self,user,pass1,pass2):


        sql =f"SELECT COUNT(Name_user) FROM users WHERE Name_user='{user}'"

        self.cursor.execute(sql)


        num=self.cursor.fetchone()[0]

        if num!=0:
            self.con.close()

            return 0

        if pass1!=pass2:
            self.con.close()

            return 1

        if num==0 and pass1==pass2:
            self.con.close()

            return 2


    def crear_usuario(self,user,pass1):

        password=hashlib.sha256(pass1.encode('utf-8')).hexdigest()

        sql=f"INSERT INTO users (Name_user,Pass) VALUES (?,?)"
        self.cursor.execute(sql,(user,password))


        self.con.commit()
        self.con.close()

    def change_weigth(self,user,peso):

        sql=f"UPDATE users SET Weight={peso} WHERE Name_user='{user}'"

        self.cursor.execute(sql)
        self.con.commit()
        


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




# con=sqlite3.connect('eat_food.db')

# cursor=con.cursor()

# sql="DROP TABLE comidas"

# sql="""CREATE TABLE IF NOT EXISTS comidas(
# id_comida integer auto_increment,
# id_user integer,
# id_alimen integer,
# p_comidas real,
# kcal_comi real,
# grasa_comi real,
# grsatu_comi real,
# carbo_comi real,
# azu_comi real,
# prote_comi real,
# sal_comi real,
# fecha date,

# primary key(id_comida,id_user,id_alimen),
# foreign key(id_user) references users(Id_user),
# foreign key(id_alimen) references alimentos(Id)

# );"""

# cursor.execute(sql)

# con.commit()
# con.close()
