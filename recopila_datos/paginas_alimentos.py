from venv import main
from bs4 import BeautifulSoup
import requests
from datos import *
import os

import time


def main():




    for i in range(426):
        print(i)
        html_text = requests.get(f'https://www.fatsecret.es/calor%C3%ADas-nutrici%C3%B3n/search?q=Hacendado&pg={i}').text

        soup = BeautifulSoup(html_text,'lxml')

        names=soup.find_all('a',class_='prominent')
        names=[i['href'] for i in names]

        for i in names:

            save_data(f'https://www.fatsecret.es{i}')

            time.sleep(0.3)






if __name__ == '__main__':

    main()


