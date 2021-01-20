from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.views.generic import CreateView

from .models import Tweet
from .forms import *



class Base(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'main.html', {'tweets':tweets})

#User login view:
class UserLogin(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'login.html', {"form": form})
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                #return redirect('/')
            else:
                return HttpResponse('Login or email invalid')
            # error info
            return redirect('/')

 #user log out:
class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')

# user register:
class UserAdd(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            User.objects.create_user(password=password1, email=email)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})


#create tweet for loged user:
class CreateTweet(LoginRequiredMixin, CreateView):
    template_name = "tweet_add.html"
    model = Tweet
    fields = ['content']

    def form_valid(self, form):
        user = self.request.user
        content = form.cleaned_data.get('content')
        Tweet.objects.create(content=content, user=user)
        return redirect('/')

#User detail site:
class UserDetails(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user_info = User.objects.get(id=user_id)
        tweets = Tweet.objects.filter(user_id=user_id)
        ctx = {
            'user_info': user_info,
            'tweets': tweets,
        }
        return render(request, 'user_side.html', ctx)

class MessageCreate(LoginRequiredMixin, CreateView):
    template_name = "message_create.html"
    model = Message
    fields = ['message_content', 'reciver']