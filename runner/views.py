from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("hello world!")

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("bootstrap3.html")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
