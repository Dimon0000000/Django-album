from django.http import HttpResponse
from django.shortcuts import render

from photo.models import Photo
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    photos = Photo.objects.all()
    paginator = Paginator(photos, 6)
    page_number = request.GET.get('page')
    paged_photos = paginator.get_page(page_number)

    context = {'photos': paged_photos}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)

        is_logout = request.POST.get('is_logout')
        if is_logout == 'True':
            logout(request)

    return render(request, 'photo/list.html', context)


def upload(request):
    if request.method == 'POST' and request.user.is_superuser:
        image = request.FILES.getlist('images')
        for i in image:
            photo = Photo(image=i)
            photo.save()
        return redirect('index')
