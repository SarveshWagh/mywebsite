from django.shortcuts import render
from django.shortcuts import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar


def index(request):
    year = date.today().year
    month = date.today().month
    month_name = calendar.month_name[month]
    title = f"Hi Sarvesh, current month is: {month_name} - {year}"
    cal = HTMLCalendar().formatmonth(year, month)
    context_data = {'title': title, 'cal': cal}
    return render(request, 'base.html', context_data)
