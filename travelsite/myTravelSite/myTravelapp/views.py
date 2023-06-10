from django.shortcuts import render
from django.http import HttpResponse
from .models import tourPics, teamPics


# Create your views here.
def index(request):
    tourPicsObj = tourPics.objects.all()
    teamPicsObj = teamPics.objects.all()
    return render(request, 'index.html', {'TourPics': tourPicsObj, 'TeamPics': teamPicsObj})


def demo(request):
    return HttpResponse('Hello World')


def login(request):
    return render(request, 'loginPage.html')


def contact(request):
    return render(request, 'contact.html')


def passVal(request):
    x = 'Saranya'
    return render(request, 'passValue.html', {'name': x})


def calcForm(request):  # This function calls the html form page to enter 2 numbers
    return render(request, 'calcForm.html')


def calcFormResult(request):  # Thsi function is to display the result in result.html page
    res1 = int(request.GET['num1']) + int(request.GET['num2'])
    res2 = int(request.GET['num1']) - int(request.GET['num2'])
    res3 = int(request.GET['num1']) * int(request.GET['num2'])
    return render(request, 'calcFormResult.html', {'add': res1, 'sub':res2, 'mul':res3 })
