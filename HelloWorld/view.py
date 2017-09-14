# -*- coding: utf-8 -*-

from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'hello workd'
	return render(request,'hello.html',context)