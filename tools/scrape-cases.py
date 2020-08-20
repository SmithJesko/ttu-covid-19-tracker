import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = 'https://www.ttuhsc.edu/safe/reported-cases.aspx'
x = requests.get(url)
soup = BeautifulSoup(x.content, 'html.parser')

row_titles = []

table = soup.table
table = soup.findAll('table')
student_rows = table[0].findAll('tr')
staff_rows = table[7].findAll('tr')

f = open('student_rows.txt', 'a')
f.write(str(datetime.now()) + '\n')
f.close()
for tr in student_rows:
    td = tr.findAll('td')
    row = [i.text for i in td]
    f = open('student_rows.txt', 'a')
    f.write(str(row) + '\n')
    f.close()

f = open('staff_rows.txt', 'a')
f.write(str(datetime.now()) + '\n')
f.close()
for tr in staff_rows:
    td = tr.findAll('td')
    row = [i.text for i in td]
    f = open('staff_rows.txt', 'a')
    f.write(str(row) + '\n')
    f.close()
