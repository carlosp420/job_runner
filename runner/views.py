from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def index(request):
    t = get_template("bootstrap3.html")
    html = t.render(Context({
            'bootstrap3_title': 'Run programs',
            }))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("bootstrap3.html")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
