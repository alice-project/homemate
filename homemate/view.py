
# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['welome'] = 'Welcome To!'
    return render(request, 'homepage.html', context)

