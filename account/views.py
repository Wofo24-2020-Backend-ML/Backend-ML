from django.shortcuts import render, redirect
from account.models import *

from django.contrib.auth.models import User
from .forms import RequestVerificationForm, CreatePackageForm, UploadImageForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

from registration.forms import ProfessionalForm, CreateUserForm, UpdateUserForm

from django.contrib import messages


@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional', 'admin'])
def home(request):
    business_name = Professional.objects.all()
    context = {"business_name": business_name}
    return render(request, "account/home.html", context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def profile(request, pk):
    professional = Professional.objects.get(user=pk)
    sub_category = professional.sub_category.all()
    context = {'professional':professional, 'subcategories':sub_category}
    return render(request, "account/profile.html", context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        professional_form = ProfessionalForm(request.POST, request.FILES, instance=request.user.professional)
        if user_form.is_valid() and professional_form.is_valid():
            user_form.save()
            professional_form.save()
            messages.success(request, "Your Profile was Updated successfully")
            return redirect('/account/')
        else:
            messages.error(request, "Please correct the error below")
    else:
        user = request.user.professional
        user_form = UpdateUserForm(instance=request.user)
        professional_form = ProfessionalForm(instance=user)
    context = {'user_form':user_form, 'professional_form':professional_form}
    return render(request, 'registration/update_profile.html', context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def upload_image(request):
    user = request.user.professional
    form = UploadImageForm(instance=user)
    if request.method == 'POST':
        form = UploadImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/account/upload_image')
    context = {'form':form}
    return render(request, "account/upload_image.html", context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def details(request, pk_test):
    detail = Professional.objects.get(id=pk_test)
    sub_category = detail.sub_category.all()
    context = {'detail':detail, 'subcategories':sub_category}
    return render(request, 'account/details.html', context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def request_verification(request):
    user = request.user.professional
    form = RequestVerificationForm(instance=user)
    if request.method == 'POST':
        form = RequestVerificationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'account/request_verification.html', context)
    


@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def create_package(request):
    user = request.user.professional
    form = CreatePackageForm(instance=user)
    if request.method == 'POST':
        form = CreatePackageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/account/')
    context = {'form':form}
    return render(request, 'account/create_package.html', context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def view_package(request, pk):
    package = Package.objects.filter(user=pk)
    context = {'package':package}
    return render(request, 'account/view_package.html', context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def update_package(request, pk1):
    package = Package.objects.get(id=pk1)
    form = CreatePackageForm(instance=package)
    if request.method == 'POST':
        form = CreatePackageForm(request.POST or None, request.FILES or None, instance=package)
        if form.is_valid():
            form.save()
            return redirect('/account/')
    context = {'form': form}
    return render(request, 'account/update_package.html', context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def delete_package(request, pk2):
    package = Package.objects.get(id=pk2)
    if request.method == 'POST':
        package.delete()
        return redirect('/account/')
    context = {'package':package}
    return render(request, 'account/delete_package.html', context)



@login_required(login_url='/login/')
@allowed_users(allowed_roles=['professional'])
def all_images(request, pk):
    images = UploadImage.objects.filter(user=pk)
    context = {'images':images}
    return render(request, 'account/all_images.html', context)


