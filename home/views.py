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
    else:
        # get_case_report()
        print('report up to date')

    cases = Cases.objects.latest('id')

    dates = []
    data = []  

    weekly_cases = Cases.objects.order_by('id')[:7]
    for case in weekly_cases:
        dates.append(case.report_date)
        data.append(case.total_active)

    context = {
        'dates': dates,
        'data': data,
        'date': cases.report_date,
        'updated': cases.name[31:],
        'students_reported': cases.students_reported,
        'students_recovered': cases.students_recovered,
        'students_active': cases.students_active,
        'faculty_reported': cases.faculty_reported,
        'faculty_recovered': cases.faculty_recovered,
        'faculty_active': cases.faculty_active,
        'total_reported': cases.total_reported,
        'total_recovered': cases.total_recovered,
        'total_active': cases.total_active,
    }

    return render(request, 'home/index.html', context)