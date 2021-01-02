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