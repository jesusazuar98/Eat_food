import json

f=open('recopila_datos/alimentos.txt','r',encoding='utf8')

alimentos={}

for i in f:

    name=['Name','Porcion','Kcal','Grasa','Grasa Saturada','Carbohidratos','Azucar','Proteina','Sal']

    valores={}

    for x in range(1,len(i.split(','))):

        num=float(i.split(',')[x])
        valores[name[x]]=num
        


    alimentos[i.split(',')[0]]=valores

f.close()


with open('recopila_datos/alimentos.json','w',encoding='utf8') as f:

    json.dump(alimentos,f,ensure_ascii=False)
