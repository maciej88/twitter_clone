from django.shortcuts import render
from django.views import View
from .models import Tweet



class Base(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'main.html', {'tweets':tweets})
