from django.shortcuts import render

import requests

from bs4 import BeautifulSoup
from datetime import datetime

from .models import Cases
from .tasks import get_case_report


def index(request):
    url = 'https://www.depts.ttu.edu/communications/emergency/coronavirus/'
    x = requests.get(url)
    soup = BeautifulSoup(x.content, 'html.parser')
    table = soup.table
    table = soup.find('table')
    title = str(table.find('h4').get_text()) + ' ' + str(table.find('em').get_text())
    report_date = str(title[68:])
    if report_date > datetime.now().strftime('%B %#d, %Y'):
        get_case_report()
        print('got report')
        return render(request, 'home/index.html', {})
    else:
        print('report up to date')
        return render(request, 'home/index.html', {})

    return render(request, 'home/index.html', {})