from django.shortcuts import render,redirect
from main_app.models import *
from main_app.forms import Contactfrom
# Create your views here.


def index(request):
    userinfo=UserInfo.objects.last()
    return render(request,'index.html',{'userinfo':userinfo})


def contact(request):
    if request.method == 'POST':
        form=Contactfrom(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Contactfrom()
    return render(request,'contact.html',{'form':form})


def projects(request):
    return render(request,'projects.html')

def resume(request):
    experience=Experience.objects.all()
    education=Education.objects.all()
    resume = Resume.objects.last()
    return render(request,'resume.html',{'experience':experience,'education':education,'resume':resume})