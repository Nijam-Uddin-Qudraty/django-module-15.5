from django.shortcuts import render, redirect
from .forms import MusicianForm, AlbumForm
from .models import Musician, Album
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .import forms

# Create your views here.


def home(req):

    albums = Album.objects.all()
    return render(req, 'home.html', {'album': albums})


def register(req):
    if req.method == "POST":
        form = forms.Register_form(req.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.Register_form()
    return render(req, 'register.html', {'form': form, 'type': 'Register'})


def user_login(req):
    if req.method == "POST":
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pas = form.cleaned_data['password']
            auth = authenticate(req, username=name, password=pas)
            if auth:
                login(req, auth)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(req, 'register.html', {'form': form, 'type': 'Login'})


@login_required
def user_logout(req):
    logout(req)
    return redirect('homepage')


@login_required
def edit(req, id):
    albums = Album.objects.get(pk=id)
    form = AlbumForm(instance=albums)
    if req.method == 'POST':
        form = AlbumForm(req.POST, instance=albums)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    return render(req, 'add_album.html', {'form': form})


@login_required
def delete(req, id):
    albums = Album.objects.get(pk=id).delete()
    return redirect("homepage")


@login_required
def add_musician(req):
    if req.method == 'POST':
        form = MusicianForm(req.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = MusicianForm()
    return render(req, 'add_musician.html', {'form': form})


@login_required
def add_album(req):
    if req.method == 'POST':
        form = AlbumForm(req.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(req, 'add_album.html', {'form': form})
