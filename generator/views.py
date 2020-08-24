# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
import random
def home(request):
    #return HttpResponse('Hello There !')
    return render(request,'generator/home.html',{'password':'dohoqwpidq17919'})
def password(request):

    length=int(request.GET.get('length',12))
    #if request.GET.get('lowercase'):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('012345679'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
