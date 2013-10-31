from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import subprocess

def index(request):
    t = get_template("bootstrap3.html")
    cpu = get_cpu_load()
    html = t.render(Context({
            'bootstrap3_title': 'Server status',
            'cpu': cpu,
            }))
    return HttpResponse(html)

def get_cpu_load():
    cmd = "uptime"
    p = subprocess.check_output(cmd, shell=True)
    p = p.strip().split(":")
    p = p[4].strip().split(",")
    free = "true"
    for i in p:
        if float(i.strip()) > 1.0:
            free = "false"
    # are the processors free?
    return free

