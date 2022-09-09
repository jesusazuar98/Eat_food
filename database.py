import sqlite3
import hashlib


class Database:

    def __init__(self):

        self.con=sqlite3.connect('eat_food.db')
        self.cursor=self.con.cursor()

    
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
    
        self.con.close()
    


    def crear_usuario(self,user,pass1):

        password=hashlib.sha256(pass1.encode('utf-8')).hexdigest()

        sql=f"INSERT INTO users (Name_user,Pass) VALUES (?,?)"
        self.cursor.execute(sql,(user,password))


        self.con.commit()
        self.con.close()



    def all_food(self):


        self.cursor.execute('SELECT * FROM alimentos')

        alimentos=self.cursor.fetchall()


        for i in alimentos:

            print(i)

            self.con.close()


# con=sqlite3.connect('eat_food.db')

# cursor=con.cursor()

# sql="""CREATE TABLE users(
# Id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
# Name_user VARCHAR(50) NOT NULL,
# Pass VARCHAR(100) NOT NULL,
# Tall_user REAL,
# Weight REAL

# );"""

# sql2='DROP TABLE users;'

# sql='ALTER TABLE users MODIFY COLUMN Pass VARCHAR(50)'

# cursor.execute(sql)

# con.close()
