from django.urls import path, include

from photo import views
from photo.views import upload

app_name = 'photo'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', upload, name='upload')
]