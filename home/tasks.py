import requests
from bs4 import BeautifulSoup

from .models import Cases

def get_case_report():
    """
    Makes a request to https://www.depts.ttu.edu/communications/emergency/coronavirus/ and scrapes case data.
    """
    url = 'https://www.depts.ttu.edu/communications/emergency/coronavirus/'
    x = requests.get(url)
    soup = BeautifulSoup(x.content, 'html.parser')
    table = soup.table
    table = soup.find('table')
    title = str(table.find('h4').get_text()) + ' ' +str(table.find('em').get_text())
    rows = table.findAll('tr')
    print(title[68:])
    all_rows = []
    for tr in rows:
        td = tr.findAll('td')
        for i in td:
            all_rows.append(i.text)
    print(all_rows)
    c = Cases.objects.create(
        name = title,
        students_reported = int(all_rows[5]),
        students_recovered = int(all_rows[9]),
        students_active = int(all_rows[13]),
        faculty_reported = int(all_rows[6]),
        faculty_recovered = int(all_rows[10]),
        faculty_active = int(all_rows[14]),
        total_reported = int(all_rows[7]),
        total_recovered = int(all_rows[11]),
        total_active = int(all_rows[15]),
        report_date = str(title[68:]),
    )
    c.save()