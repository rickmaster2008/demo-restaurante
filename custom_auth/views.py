from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

from .forms import LoginForm

class Login(View):
    template_name = 'custom_auth/login.html'

    def get(self, req, *args, **kwargs):
        context = {
            'form': LoginForm()
        }
        return render(req, self.template_name, context)
    
    def post(self, req, *args, **kwargs):
        form = LoginForm(req.POST)
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            return redirect('login')