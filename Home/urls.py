from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='index'),
    path("index", views.index, name='home'),
    path("about", views.about, name='about'),
    path("faq", views.faq, name='faq'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("scan", views.scan, name='scan')
]