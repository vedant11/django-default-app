from django.shortcuts import render

def homepage(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def projects(request):
	return render(request,'projects.html')

def contacts(request):
	return render(request,'contacts.html')
