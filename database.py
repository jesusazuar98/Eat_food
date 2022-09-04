import sqlite3


class Database:

    def __init__(self):

        self.con=sqlite3.connect('eat_food.db')

        self.cursor=self.con.cursor()

    def all_food(self):

        self.cursor.execute('SELECT * FROM alimentos')

        alimentos=self.cursor.fetchall()


        for i in alimentos:

            print(i)

            self.con.close()

