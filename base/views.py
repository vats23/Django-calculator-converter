from django.shortcuts import render
import os
# Create your views here
def base(request):
    return render(request,'basic.html')
