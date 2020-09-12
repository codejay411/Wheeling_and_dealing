from django.shortcuts import render, HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages



# username- admin password- admin@1234   <------  Superuser
# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

def registerpage(request):
    form = CreateUserForm()
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)
    # return HttpResponse("this is register page")

def loginpage(request):
    return render(request, 'login.html')
    # return HttpResponse("this is login page")

def logoutuser(request):
    return HttpResponse("this is logout page")

def aboutus(request):
    return render(request, 'about-us.html')
    # return HttpResponse("this is logout page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is logout page")

