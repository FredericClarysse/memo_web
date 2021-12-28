from flashcard import views
from django.urls import path

app_name = 'flashcard'

urlpatterns = [
    path('', views.home, name='home')
]