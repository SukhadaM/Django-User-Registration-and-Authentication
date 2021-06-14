from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

# def login(request):
#     return render(request,'login.html')

# def register(request):
#     return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.SUCCESS, 'You have now logged in successfully')
            return redirect('accounts:dashboard-profile')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('accounts:login')
   
    else:
        return render(request,'login.html')
   
   


def register(request):
    if request.method =='POST':
        # messages.add_message(request, messages.ERROR, 'Username taken')
        # return redirect('register')
        address=request.POST['address']
        username=request.POST.get('username')
        email=request.POST['email']
        address=request.POST['address']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username taken')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist')
                    return redirect('accounts:register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=address)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'You are now register,please log in')
                    return redirect('accounts:login')
                
        else:
            messages.add_message(request, messages.ERROR, 'Passwords does not match')
            return redirect('accounts:register')
    
        
    return render(request,'register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out successfullt')
        return redirect('login')
    
    return redirect('login')

def dashboardprofile(request):
    return render(request,'dashboardprofile.html')



# def editprofile(request):
#     if request.method =='POST':
#         email = request.POST.get('email')
#         user_details = User.objects.get(email=email)
#         password =  request.POST.get('password')
#         new_email = user_details.email
#         new_address = user_details.first_name
#         new_username = user_details.username
#         new_username = request.POST['username']
#         new_address = request.POST['address']
#         User.objects.get(email=email).delete()
#         user=User.objects.create_user(username=new_username,password=password,email=new_email,first_name=new_address)
#         user.save()
#         return redirect('accounts:login')
#     return render(request, 'editprofile.html')

def changeemail(request):
    if request.method == 'POST':
        old_email = request.POST.get('old_email')
        new_email = request.POST.get('new_email')
        password = request.POST.get('password')
        user_details = User.objects.get(email=old_email)
        new_username = user_details.username
        new_address = user_details.first_name
        user_auth=auth.authenticate(username=new_username,password=password)
        if user_auth:
            if User.objects.filter(email=new_email).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist')
                    return redirect('accounts:change-email')
            else:
                User.objects.get(email=old_email).delete()
                User.objects.create_user(username=new_username,password=password,email=new_email,first_name=new_address).save()
                return redirect('accounts:login')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('accounts:change-username')
    return render(request, 'changeemail.html')
    

def changeusername(request):
    if request.method == 'POST':
        username = request.POST.get('old_username')
        new_username = request.POST.get('new_username')
        password = request.POST.get('password')
        user_details = User.objects.get(username=username)
        new_email = user_details.email
        new_address = user_details.first_name
        user_auth=auth.authenticate(username=username,password=password)
        if user_auth:
            if User.objects.filter(username=new_username).exists():
                    messages.add_message(request, messages.ERROR, 'Email Already Exist')
                    return redirect('accounts:change-username')
            else:
                User.objects.get(username=username).delete()
                User.objects.create_user(username=new_username,password=password,email=new_email,first_name=new_address).save()
                return redirect('accounts:login')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('accounts:change-username')
    return render(request, 'changeusername.html')


def changeaddress(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_address = request.POST.get('new_address')
        password = request.POST.get('password')
        user_details = User.objects.get(username=username)
        new_email = user_details.email
        User.objects.get(username=username).delete()
        User.objects.create_user(username=username,password=password,email=new_email,first_name=new_address).save()
        return redirect('accounts:login')
    return render(request, 'changeaddress.html')

def deleteprofile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        User.objects.get(username=username).delete()
        return redirect('accounts:register')
    return render(request, 'deleteprofile.html')


