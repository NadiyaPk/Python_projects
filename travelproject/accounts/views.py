from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method=='POST':
           form=UserCreationForm(request.POST)
           if form.is_valid():
             form.save()
             return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, "register.html", {'form': form})
def login(requset):
    return(requset,'login.html')
    # if request.method=='POST':
    #     username=request.POST['username']
    #     first_name=request.POST['first _name']
    #     last_name=request.POST['last_name']
    #     email=request.POST['email']
    #     password=request.POST['password']
    #     copassword=request.POST['password1']
    #     user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
    #     user.save();
    #     print("user created")
