from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    form = forms.Two()
    fun=0
    sub=False
    if request.method =="POST":
        form = forms.Two(request.POST)
        if form.is_valid():
            n1=form.cleaned_data['n1']
            n2=form.cleaned_data['n2']
            if request.POST.get("add"):
                fun=n1+n2
            if request.POST.get("subtract"):
                fun=n1-n2
            if request.POST.get("multiply"):
                fun=n1*n2
            if request.POST.get("divide"):
                fun=n1/n2
            if request.POST.get("modulo"):
                fun=n1%n2
            sub=True
    return render(request,'calculator/index.html',{'form':form,'fun':fun,'submitted':sub})
