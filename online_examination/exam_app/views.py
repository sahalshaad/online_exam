from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import Login, StudentSignup, TeacherSignup

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup_student(request):
    return render(request, 'signup_student.html')

def signup_student_post(request):
    print(request.POST) 
    name = request.POST.get('name')
    clas = request.POST.get('clas')
    rollno = request.POST.get('rollnumber')
    dob = request.POST.get('dob')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if Login.objects.filter(username=username).exists():
        return HttpResponse('''<script>alert("Username already taken! Please choose a different one.");window.location="/signup_student/"</script>''')

    student_login = Login()
    student_login.username = username
    student_login.password = make_password(password)
    student_login.type = 'student'
    student_login.save()

    signup = StudentSignup(
        name = name,
        clas = clas,
        rollno = rollno,
        dob = dob,
        username = username,
        password = make_password(password),
        login = student_login,
    )
    signup.save()

    return HttpResponse('''<script>alert("Signup Successfully");window.location="/login/"</script>''')

def signup_teacher(request):
    return render(request, 'signup_teacher.html')

def signup_teacher_post(request):
    name = request.POST['name']
    department = request.POST['department']
    phone = request.POST['phonenumber']
    username = request.POST['username']
    password = request.POST['password']

    if Login.objects.filter(username=username).exists():
        return HttpResponse('''<script>alert("Username already taken! Please choose a different one.");window.location="/signup_teacher/"</script>''')

    teacher_login = Login()
    teacher_login.username = username
    teacher_login.password = make_password(password)
    teacher_login.type = 'teacher'
    teacher_login.save()

    teacher = TeacherSignup(
        name = name,
        department = department,
        phonenumber = phone,
        username = username,
        password = make_password(password),
        login = teacher_login,
    )
    teacher.save()

    return HttpResponse('''<script>alert("Teacher Signup Successfully");window.location="/login/"</script>''')

def login_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = Login.objects.filter(username=username).first()

    if user and check_password(password, user.password):
        request.session['lid'] = user.id

        if user.type == 'student':
            return HttpResponse('''<script>alert("Student LogIn Successfully");window.location="/student_dashboard/"</script>''')
        elif user.type == 'teacher':
            return HttpResponse('''<script>alert("Teacher LogIn Successfully");window.location="/teacher_dashboard/"</script>''')
        else:
            return HttpResponse('''<script>alert("Unknown User Type");window.location="/"</script>''')
    else:
        return HttpResponse('''<script>alert("LogIn Failed");window.location="/"</script>''')