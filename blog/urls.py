from blog import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home')
]