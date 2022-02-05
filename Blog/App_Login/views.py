from django.shortcuts import render

# Create your views here.

def Signup(request):
    return render(request, 'App_Login/signup.html', context={})
