from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,TemplateView
from .models import CustomUser
from django.http import HttpResponseRedirect
from .forms import CustomUserForm, UpdateSettingsForm, UpdatePasswordForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse
from django.contrib import messages
# Create your views here
def home(request):
    return(render(request,'home.html'))

# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

class AccountsHome(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'

def create_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,'You have successfully registered! Please continue to your dashboard!')
            return HttpResponseRedirect('/accounts/login/')
        else:
            print('Not valid here',form.errors)
            pass
            #if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_user(request):
    if request.method =='POST':
        userEmail = request.POST['email']
        userPassword = request.POST['password']
        user = authenticate(username=userEmail,password=userPassword)
        if user is not None:
            login(request,user)
            messages.add_message(request,messages.INFO,'You have successfully logged in! Please continue to your dashboard!')
            return HttpResponseRedirect(reverse('accounts:home'))
        else:
            messages.add_message(request, messages.ERROR,'Invalid credentials provided, failed to login!')
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        return render(request, 'accounts/login.html',{})

def logout_view(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,
                    'Successfully logged out, Please login to continue!')
    return HttpResponseRedirect(reverse('accounts:login'))