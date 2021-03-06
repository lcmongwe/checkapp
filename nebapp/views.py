from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
import datetime as dt
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


# authentication
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .forms import RegisterUserForm

@login_required(login_url='login')
def home(request):
    location1=request.user.location
    posts=Post.objects.all().filter(location=location1)

    return render(request, 'main/home.html', {'posts': posts,})

@login_required(login_url='login')
def all_posts(request):
    posts=Post.objects.all()

    return render(request, 'main/all_posts.html', {'posts': posts,})

@login_required(login_url='login')
def delete_post( request,pk):
    post=Post.objects.get(id=pk)

    if request.method=='POST':
        if request.user==post.author:
            post.delete()
            return redirect('home')
        else:
            messages.success(request,('you are not allowed to delete this event'))
        
    return render(request, 'main/delete.html', {'post':post})

@login_required(login_url='login')
def facilities(request):
    location=request.user.location
    facilities=Business.objects.all().filter(location=location)

    return render(request, 'main/facilities.html', {'facilities': facilities})

def profile(request,pk):
    user = User.objects.get(id=pk)
    location=request.user.location
    facilities=Business.objects.all().filter(location=location)

    return render(request, 'main/profile.html', {'user': user,'facilities': facilities})



def update_profile(request,user_id):
    user=User.objects.get(pk=user_id)
    user1=request.user
    form=RegisterUserForm(request.POST,request.FILES, instance=user)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/update_profile.html',{'user':user,'form':form})



@login_required(login_url='login')
def create_post(request):
    form=CreatePostForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,(' posted successfully!'))
        
        return redirect('home')
    return render(request, 'main/post.html', {'form': form})

@login_required(login_url='login')
def create_biz(request):
    form=FacForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        messages.success(request,(' posted successfully!'))
        
        return redirect('home')
    return render(request, 'main/createfac.html', {'form': form})


def search_biz(request):
    if request.method == 'POST':
        searched=request.POST.get('searched')
        posts=Business.objects.filter(name__contains=searched)
        return render(request, 'main/searched.html',{'searched':searched,'posts':posts})
       
    else:
        return render(request, 'main/searched.html',{})




# AUTHENTICATION
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('there ws an error loggig in, please try again...'))
            return redirect('login')

    else:
        return render (request,'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,('you are logged out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form =RegisterUserForm(request.POST)
        if form.is_valid():

            username=request.POST['username']
            email=request.POST['email']
            subject='welcome to InstaApp'
            message=f'Hi {username} welcome to InstaApp and have fun! '
            from_email=settings.EMAIL_HOST_USER
            recipients=[email]
            # send_mail(subject, message,from_email,recipients)

            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('Regestration succesful'))
            return redirect('home')
    else:
        form =RegisterUserForm()


    return render(request,'authenticate/register.html',{'form':form,})