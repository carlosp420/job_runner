from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

from django import forms

def upload_file(request):
    if request.method == "POST":
        form = RunForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect("/success")
        else:
            form = RunForm()
        return render_to_response("upload.html", {'form', form})

class RunForm(forms.Form):
    xml_beauty_file = forms.FileField()

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
    form = RunForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect("/thanks/")
    else:
        form = RunForm()

    t = get_template("bootstrap3.html")
    html = t.render(Context({
            'bootstrap3_title': 'Running ' + name,
            'form': form,
            }))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("bootstrap3.html")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


