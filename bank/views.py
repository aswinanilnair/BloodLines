from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from bank.forms import UserForm,UserProfileInfoForm,BlogPostForm
from bank.models import BlogPost
#don't forget to add your models


# Create your views here.
def index(request):
    return render(request,'bank/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # one to one relationship defined here.
            profile.user = user

            if 'img' in request.FILES:
                profile.img = request.FILES['img']


            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'bank/registration.html',
                                        {'user_form':user_form,
                                         'profile_form':profile_form,
                                         'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active!!")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'bank/login.html',{})


def newPost(request):
    if request.method =='POST':
        blog_form = BlogPostForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            if 'blog_img' in request.FILES:
                blog.img = request.FILES['blog_img']


            blog.save()
            return HttpResponseRedirect(reverse('blog'))

        else:
            print(blog_form.errors)
    else:
        blog_form = BlogPostForm()

    return render(request,'bank/newpostForm.html',{'blog_form':blog_form})

@login_required
def requestBlood(request):
    return render(request,'bank/request.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def blogpage(request):
    blogs = BlogPost.objects.all()
    return render(request,'bank/blog.html',{'blogs':blogs})


def make_request(request):
   return HttpResponse("Request Page Coming Up!!")
