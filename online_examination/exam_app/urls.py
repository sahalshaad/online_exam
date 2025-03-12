from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup_student/', views.signup_student, name='signup_student'),
    path('signup_student_post/', views.signup_student_post, name='signup_student_post'),
    path('signup_teacher/', views.signup_teacher, name='signup_teacher'),
    path('signup_teacher_post/', views.signup_teacher_post, name='signup_teacher_post'),
    path('login_post/', views.login_post, name='login_post'),
]