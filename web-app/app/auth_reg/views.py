from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from .forms import RegisterForm, EditProfileForm, RecordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash

from .models import *


def register_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = RegisterForm()
    return render(request, "auth_reg/registration.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = AuthenticationForm()
    return render(request, "auth_reg/auth.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def profile(request, username):
    return render(request, 'auth_reg/profile.html', {'username': username})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            if form.cleaned_data['new_password1']:
                request.user.set_password(form.cleaned_data['new_password1'])
            form.save()
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Профиль обновлен')
            return redirect('profile', {'user': request.user})
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'auth_reg/edit_profile.html', {'form': form})


def laboratory_seven(request):
    longitude = Longitude.objects.all()
    latitude = Latitude.objects.all()
    city = City.objects.all()
    device = Device.objects.all()
    measurements = Measurements.objects.all()
    context = {'longitude': longitude, 'latitude': latitude, 'city': city, 'device': device, 'measurements': measurements}
    return render(request, 'auth_reg/laboratory_seven.html', context)

def create_record(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab7')
        else:
            error = 'Ошибка добавления записи'
            return redirect('lab7')
    form = RecordForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'auth_reg/create_record.html', data)


def delete_rec(request, el_id):
    event = Measurements.objects.get(pk=el_id)
    event.delete()
    return redirect('lab7')


class UpdateRecord(UpdateView):
    model = Measurements
    template_name = 'auth_reg/update_record.html'
    fields = ['id', 'city', 'device', 'temperature']
    success_url = reverse_lazy("lab7")