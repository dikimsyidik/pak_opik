from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render
def logout_views(request):
    logout(request)
    return HttpResponseRedirect('/')

def home(request):
	return render(request,'home.html')

def perusahaan(request):
	return render(request,'perusahaan.html')