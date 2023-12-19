from django.http import HttpResponse
from django.shortcuts import render


# Create your views her




def home(request):
    return render(request,"index1.html")
