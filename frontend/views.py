from django.shortcuts import render
from api1.models import EndPoints
import random

def HomePage(request):
    data = EndPoints.objects.filter(is_active=True)
    colors = ["info", "success", "warning", "danger","secondary"]
    random.shuffle(colors)
    data_and_colors = zip(data, colors)
    context = {
        'data':data_and_colors
    }
    return render(request,"frontend/home/index.html",context)

def EndPointView(request,slug):
    data = EndPoints.objects.filter(is_active=True,slug=slug).first()
    colors = ["info", "success", "warning","secondary"]
    random.shuffle(colors)
    context = {
        'data':data,
        'color':colors[0]
    }
    return render(request,"frontend/home/detailed_view.html",context)

def TestPage(request):
    return render(request,"frontend/home/test.html")