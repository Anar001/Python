from bs4 import BeautifulSoup
import requests
import time

Start = time.perf_counter()

resp = requests.get("https://yandex.ru/")
soup = BeautifulSoup(resp.text, 'lxml')

print('\n',soup.title,'\n')
print(soup.title.text,'\n')

Stop = time.perf_counter()
print(f'Время выполнения программы: {round(Stop-Start,3)}')