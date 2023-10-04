from bs4 import BeautifulSoup
import requests

list_city = []

def write_txt(line):
    file = open('list_city.txt', 'a')
    file.writelines(line+'\n')
    file.close()

url = 'https://ru.wikipedia.org/wiki/Список_городов_России'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')

block = bs.find_all('tbody')[0]
for b in block.find_all('tr'):
    stop = 0
    time_list = ''
    for l in b.find_all('td'):
        if stop == 2 or stop == 3:
            if time_list == '':
                time_list += l.get_text()
            else:
                time_list += ' - ' + l.get_text()
        stop += 1
    list_city.append(time_list)

for lc in list_city:
    write_txt(lc)
