from django.shortcuts import render,redirect
from .froms import MusicianForm,AlbumForm
from .models import Musician,Album
# Create your views here.
def home(req):
    
    albums = Album.objects.all()
    return render(req, 'home.html' ,{'album':albums})

def edit(req,id):
    albums = Album.objects.get(pk=id)
    form = AlbumForm(instance=albums)
    if req.method == 'POST':
        form = AlbumForm(req.POST,instance=albums)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    return render(req,'add_album.html', {'form':form})
def delete(req,id):
    albums = Album.objects.get(pk=id).delete()
    return redirect("homepage")




def add_musician(req):
    if req.method == 'POST':
        form = MusicianForm(req.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = MusicianForm()
    return render(req,'add_musician.html', {'form':form})
def add_album(req):
    if req.method == 'POST':
        form = AlbumForm(req.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(req,'add_album.html', {'form':form})