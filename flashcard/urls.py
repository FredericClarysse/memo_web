from flashcard import views
from django.urls import path

app_name = 'flashcard'

urlpatterns = [
    path('', views.home, name='home'),

    # returns JSON subjects + template
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/ajax/', views.subjects_ajax, name='subjects-ajax'),
    path('subjects/ajax/<query>/', views.subjects_ajax, name='subjects-ajax'),

    # returns specific subject
    path('<subject_slug>/', views.subject_page, name='subject-page'),
    # return test data about a specific subject
    path('<subject_slug>/ajax/', views.subject_testing_data, name='subject-testing-data'),



    # return question about a specific subject
    # path('<subject_slug>/question/<question_id>/', views.subject_question_ajax, name='subject-question-ajax'),
]