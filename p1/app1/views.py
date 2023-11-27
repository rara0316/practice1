from django.shortcuts import render

def main(request):
  return render(request, 'main.html')

def register(request):
  return render(request, 'registration/register.html')

def login(request):
  return render(request, 'login.html')

