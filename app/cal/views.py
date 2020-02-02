from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm

from django.contrib.auth.decorators import login_required

@login_required()
def calendar_view(request, room_pk):
    context = {}

    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month, room_pk)
    html_cal = cal.formatmonth(withyear=True)

    context['calendar'] = mark_safe(html_cal)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)
    context['pk'] = room_pk

    return render(request, "cal/calendar.html", context)


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
