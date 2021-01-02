from django.shortcuts import render
from django.views import View
from .models import Tweet



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
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            user = authenticate(email=email, password1=password1, password2=password2)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})