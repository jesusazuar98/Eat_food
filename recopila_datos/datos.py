from multiprocessing.sharedctypes import Value
from unicodedata import name
from bs4 import BeautifulSoup
import requests



def subcadena(cadena):

    if '(' in cadena:
        
        posicion=cadena.index('(')

        return cadena[posicion+1:len(cadena)-1]

    else:

        return cadena


def insertar_txt(datos):

    datos=[datos[i] for i in datos]

    datos=",".join(datos)

    f=open('recopila_datos/alimentos.txt', 'r',encoding='utf8')

    if f.read()=='':
    

        f.close()
        f=open('recopila_datos/alimentos.txt', 'a',encoding='utf8')
        f.write(datos)
        f.close()
    
    else:
        
        f=open('recopila_datos/alimentos.txt', 'a',encoding='utf8')
        f.write('\n'+datos)
        f.close()




def save_data(url):

    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text,'lxml')

    name_food=soup.find('h1').text
    marca_food=soup.find('h2').text.lower()


    food=soup.find('td', class_="factPanel")

    value_portion =food.find('div', class_="serving_size black serving_size_value").text

    kcal=food.find('div', class_="nutrient left tRight w2").text
    elementos=food.find_all('div',class_="nutrient black left tRight w2")
    elementos=elementos[1:]
    elementos=[i.text.replace('g','').replace('-','0') for i in elementos]
    elementos.insert(0,name_food.translate(str.maketrans({'á':'a','é':'e','í':'i','ó':'o','ú':'u'}))+" ("+marca_food+")")
    elementos.insert(1,value_portion.replace('g','').replace(' ','').replace('ml',''))
    elementos.insert(2,kcal.replace('kcal','').replace(' ',''))


    name=['Name','Porcion','Kcal','Grasa','Grasa Saturada','Carbohidratos','Azucar','Proteina','Sal']
    
    valores={name[i]:elementos[i].replace(',','.') for i in range(9)}
    valores['Porcion']=subcadena(valores['Porcion'])


    
    print(valores)
    #insertar_txt(valores)




