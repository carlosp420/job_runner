from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import subprocess
import psutil

def index(request):
    t = get_template("bootstrap3.html")
    cpu = get_cpu_load()
    html = t.render(Context({
            'bootstrap3_title': 'Server status',
            'cpu': cpu,
            }))
    return HttpResponse(html)

def get_cpu_load():
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    out_cpu = []
    for i in cpu:
        if i < 26:
            out = "<span style='color:green;'>"
            out += str(i) + "%</span>"
        elif i > 74:
            out = "<span style='color:red;'>"
            out += str(i) + "%</span>"
        else:
            out = "<span style='color:yellow;'>"
            out += str(i) + "%</span>"
        out_cpu.append(out)

    out = ""
    for i in out_cpu:
        out += i + ", "
    return out


