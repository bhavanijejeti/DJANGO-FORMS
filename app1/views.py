from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def djforms(request):
    sufo=signupforms()
    d={'sufo':sufo}
    if request.method=='POST':
        sufdt=signupforms(request.POST)
        if sufdt.is_valid():
            name=sufdt.cleaned_data['name']
            return HttpResponse(str(sufdt.cleaned_data))
    return render(request,'djforms.html',d)

