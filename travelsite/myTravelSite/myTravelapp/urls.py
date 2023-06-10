from django.urls import path, include

from myTravelapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('loginPage/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('passValue/', views.passVal, name='passVal'),
    path("calc/", views.calcForm, name="calcForm"),
    path('calc/add/', views.calcFormResult, name='calcFormResult')

]
