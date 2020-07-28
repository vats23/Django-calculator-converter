from django.shortcuts import render
from . import forms
# Create your views here.
def indexbin(request):
    form = forms.conv()
    fun=0
    converted = False
    if request.method == "POST":
        form = forms.conv(request.POST)
        if form.is_valid():
            fun = int(form.cleaned_data['s1'],2)

    return render(request,'converter/indexbin.html',{'form':form,'fun':fun})

def indexdeci(request):
    form = forms.deci()
    fun=0
    converted = False
    if request.method == "POST":
        form = forms.deci(request.POST)
        if form.is_valid():
            fun = bin(form.cleaned_data['s1'])

    return render(request,'converter/indexdeci.html',{'form':form,'fun':fun})
