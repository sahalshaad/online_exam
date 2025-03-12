from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup_student/', views.signup_student, name='signup_student'),
    path('signup_student_post/', views.signup_student_post, name='signup_student_post'),
    path('signup_teacher/', views.signup_teacher, name='signup_teacher'),
    path('signup_teacher_post/', views.signup_teacher_post, name='signup_teacher_post'),
    path('login_post/', views.login_post, name='login_post'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]
