from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    return render (request, 'index.html')

def login(request):
    return render (request, 'login.html')

def signup_student(request):
    return render (request, 'signup_student.html')

def signup_student_post(request):
    name = request.POST['name']
    clas = request.POST['name']
    rollno = request.POST['name']
    dob = request.POST['name']
    username = request.POST['name']
    password = request.POST['name']
    
    if login.objects.filter(username=username).exists():
        return HttpResponse('''<script>alert("Username already taken! Please choose a different one.");window.location="/usr_signup_load/"</script>''')
    
    student_login=login()
    student_login.username = username
    student_login.password = password
    student_login.type = 'student'
    student_login.save()
    
    signup = student_signup()
    signup.name = name
    signup.clas = clas
    signup.rollno = rollno
    signup.dob = dob
    signup.username = username
    signup.password = password
    signup.login=student_login
    signup.save()
    return HttpResponse ('''<script>alert("Signup Successfully");window.location="//"</script>''')

def signup_teacher(request):
    return render (request, 'signup_teacher.html')