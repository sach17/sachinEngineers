from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User

def home(request):
	context = locals()
	template = "home.html"
	return render(request, template,context)