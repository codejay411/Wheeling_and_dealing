from django.shortcuts import render, HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .forms import CreateUserForm, CreatengoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decoraters import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .models import ngodetail, donordetail, medicine
from datetime import date
from django.contrib.auth.models import User
from django.contrib import auth



# username- admin password- admin@1234   <------  Superuser
# Create your views here.
@unauthenticated_user
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")

@unauthenticated_user
def registerdonor(request):
    form = CreateUserForm()
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            # create group
            group=Group.objects.get(name='donor')
            user.groups.add(group)
            donordetail.objects.create(
                user=user
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registerdonor.html', context)
    # return HttpResponse("this is register page")

@unauthenticated_user
def registerngo(request):
    form = CreatengoForm()
    if(request.method == 'POST'):
        form = CreatengoForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            group=Group.objects.get(name='ngo')
            user.groups.add(group)
            ngodetail.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registerngo.html', context)
    # return HttpResponse("this is register page")

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/admindashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)
    # return HttpResponse("this is login page")

def logoutuser(request):
    logout(request)
    return redirect('login')
    # return HttpResponse("this is logout page")

@unauthenticated_user
def aboutus(request):
    return render(request, 'about-us.html')
    # return HttpResponse("this is logout page")

@unauthenticated_user
def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['ngo'])
def detailsngo(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        city = request.POST['city'] 
        state = request.POST['state'] 
        address = request.POST['address'] 
        phone = request.POST['phone'] 
        authority = request.POST['authority'] 
        registrationnum = request.POST.get('registrationnum')
        # print(name, city, state)

        details=ngodetail(name=name, city=city, state=state, address=address, phone=phone, authority=authority, registrationnum=registrationnum)

        details.save()
        return render(request, 'NGOdashboard1.html')



    return render(request, 'detailsngo.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def detailsdonor(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        city = request.POST['city'] 
        state = request.POST['state'] 
        address = request.POST['address'] 
        phone = request.POST['phone'] 

        details=donordetail(name=name, city=city, state=state, address=address, phone=phone)

        details.save()
        return render(request, 'donorDashboard1.html')

    return render(request, 'detailsdonor.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@admin_only
def adminaction(request):
    return render(request, 'adminaction.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@admin_only
def admindashboard(request):
    donors=donordetail.objects.all()
    ngos=ngodetail.objects.all()

    total_donors= donors.count()
    total_ngo= ngos.count()
    context={'donors':donors, 'ngos':ngos, 'total_donors':total_donors, 'total_ngo':total_ngo}
    return render(request, 'admindashboard1.html', context)
    # return HttpResponse("this is logout page")


@login_required(login_url='login')
@allowed_users(allowed_roles=['ngo'])
def ngodashboard(request):
    donors=donordetail.objects.all()
    ngos=ngodetail.objects.all()

    total_donors= donors.count()
    sum=total_ngo+total_donors
    context={'total_donors':total_donors, 'total_ngo':total_ngo, 'sum':sum}
    # posts=postngo.objects.all()
    # if request.method=='POST':
    #     desc = request.POST['desc']
    #     user = request.user.username 
    #     print(user)
    #     # post.objects.create(
    #     #     user=user
    #     # )
    #     c=postngo(desc=desc)
    #     c.save()

    #     posts=postngo.objects.all()

    #     no_of_ngo=ngodetail.objects.all()
    #     total_ngo=no_of_ngo.count()

    #     # name=donordetail.object

    # context={'posts':posts}
        


    return render(request, 'NGOdashboard1.html', context)
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def donordashboard(request):
    donors=donordetail.objects.all()
    ngos=ngodetail.objects.all()

    total_donors= donors.count()
    total_ngo= ngos.count()
    sum=total_ngo+total_donors
    context={'total_donors':total_donors, 'total_ngo':total_ngo, 'sum':sum}
    # posts=post.objects.all()
    # if request.method=='POST':
    #     desc = request.POST['desc']
    #     user = request.user.username 
    #     print(user)
    #     # post.objects.create(
    #     #     user=user
    #     # )
    #     c=post(desc=desc)
    #     c.save()

    #     posts=post.objects.all()

    #     no_of_ngo=ngodetail.objects.all()
    #     total_ngo=no_of_ngo.count()

    #     # name=donordetail.object

    # context={'posts':posts}
        

    return render(request, 'donorDashboard1.html', context)
    # return HttpResponse("this is logout page")


@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def donorprofile(request):
    donors=donordetail.objects.all()
    context={'donors':donors}

    return render(request, 'donorprofile.html', context)
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['ngo'])
def ngoprofile(request):

    return render(request, 'ngoprofile.html')
    # return HttpResponse("this is logout page")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def medicinedonation(request):
    if request.method == 'POST':
        medicinename = request.POST['medicinename'] 
        companyname = request.POST['companyname'] 
        manufacturing = request.POST['manufacturing'] 
        expiry = request.POST['addexpiryress'] 
        tablets = request.POST['tablets'] 

        details=medicine(medicinename=medicinename, companyname=companyname, manufacturing=manufacturing, expiry=expiry, tablets=tablets)

        details.save()
        return render(request, 'donorDashboard1.html')
    return render(request, 'MedicineDonation.html')
    # return HttpResponse("this is logout page")