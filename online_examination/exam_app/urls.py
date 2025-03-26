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
    path('students_list/', views.students_list, name='students_list'),
    path('student_edit/', views.student_edit, name='student_edit'),
    path('student_edit_post/', views.student_edit_post, name='student_edit_post'),
    
    path('add_exam/', views.add_exam, name='add_exam'),
    path('add_exam_post/', views.add_exam_post, name='add_exam_post'),
    path('upload_exam_post/', views.upload_exam_post, name='upload_exam_post'),
    
    path('upload_exam/', views.upload_exam, name='upload_exam'),
    path('upload_exam/<int:exam_id>/', views.upload_exam, name='upload_exam_with_id'),
    
    path('all_exam/', views.all_exam, name='all_exam'),
    path('todays_exam/', views.todays_exam, name='todays_exam'),
    path('studyMeteriel/', views.studyMeteriel, name='studyMeteriel'),
    path('question_paper/', views.question_paper, name='question_paper'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
]
