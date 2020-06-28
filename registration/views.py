from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm, ProfessionalForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user

# Create your views here.
def home(request):
    return render(request, 'registration/home.html')


@unauthenticated_user
def register_page(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        professional_form = ProfessionalForm(request.POST, request.FILES)
        if user_form.is_valid() and professional_form.is_valid():
            user = user_form.save()
            professional_form = ProfessionalForm(request.POST, request.FILES, instance=user.professional)
            professional_form.full_clean()
            professional_form.save()
            messages.success(request, "Your Profile was Created successfully")
        else:
            messages.error(request, "Please correct the error below")
    else:
        user_form = CreateUserForm()
        professional_form = ProfessionalForm()
    context = {'user_form':user_form, 'professional_form':professional_form}
    return render(request, 'registration/register_page.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/account/')
        else:
            messages.info(request, "Username or Password incorrect")
    context = {}
    return render(request, 'registration/login_page.html', context)


def logout_page(request):
    logout(request)
    return redirect('/login/')