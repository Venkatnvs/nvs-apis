from django.shortcuts import render

def HomePage(request):
    return render(request,"frontend/home/index.html")


def TestPage(request):
    return render(request,"frontend/home/test.html")