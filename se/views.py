from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
	context = locals()
	template = "se/home.html"
	return render(request, template ,context)

def profile(request):
	context = locals()
	template = "se/profile.html"
	return render(request, template ,context)

def approach(request):
	context = locals()
	template = "se/approach.html"
	return render(request, template ,context)

def detail(request, question_id=0):
	context = locals()	
	template = "se/home.html"
	html_ = "d f"
	html_va = "<b>jjn knjjkk <b>"
	# print(request)
	return render(request, template ,context)