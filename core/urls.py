from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('sign-up/', views.sign_up, name='sign-up'),
]