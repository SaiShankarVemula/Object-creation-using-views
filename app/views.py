from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    
    tn=input('enter Topic: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('<h1> Topic is given</h1>')

def insert_webpage(request):
    tn=input('enter Topic: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    cn=input('enter name: ')
    un=input('enter the url: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=cn,url=un)[0]
    WO.save()
    return HttpResponse('<h1> Webpage Object is created</h1>')

def insert_accessrecord(request):
    tn=input('enter Topic: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    cn=input('enter name: ')
    un=input('enter the url: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=cn,url=un)[0]
    WO.save()
    dn=input('enter Date: ')
    an=input('enter Author_name: ')
    AO=AccessRecord.objects.get_or_create(name=WO,date=dn,author=an)[0]
    AO.save()
    return HttpResponse('<h1> Access record is done</h1>')