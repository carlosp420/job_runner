from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def index(request):
    from runner.models import Software
    software_list = []
    for i in Software.objects.all():
        i = str(i).split("|")
        software_list.append(i)

    t = get_template("bootstrap3.html")
    html = t.render(Context({
            'bootstrap3_title': 'Run programs',
            'software_list': software_list,
            }))
    return HttpResponse(html)

def software(request, name):
    t = get_template("bootstrap3.html")
    html = t.render(Context({
            'bootstrap3_title': 'Running ' + name,
            }))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("bootstrap3.html")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

