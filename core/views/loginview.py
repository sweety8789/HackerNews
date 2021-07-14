from django.http import HttpResponse
from django.shortcuts import render,redirect


from django.contrib.auth.models import User



def home(request):
    return render(request, 'static.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


def handlesignup(request):
    if request.method =='POST':
        email = request.POST['email']
        Password = request.POST['Password']
        ConfirmPassword = request.POST['ConfirmPassword']

        myuser = User.objects.create_user(email,Password)
        myuser.save()
        return redirect('home')

    else:
        return HttpResponse('404-Not Found')

