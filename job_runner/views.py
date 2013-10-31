from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def home(request):
    t = get_template("home.html")
    html = t.render(Context({
            "bootstrap3_title": "Home",
            }))
    return HttpResponse(html)
