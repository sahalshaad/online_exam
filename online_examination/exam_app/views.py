from venv import logger
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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
    image = request.FILES.get('photo')
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
        image = image,
    )
    signup.save()

    return HttpResponse('''<script>alert("Signup Successfully");window.location="/login/"</script>''')

def signup_teacher(request):
    return render(request, 'signup_teacher.html')

def signup_teacher_post(request):
    name = request.POST['name']
    department = request.POST['department']
    phone = request.POST['phonenumber']
    image = request.FILES.get('photo')
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
        image = image,
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
    
def student_dashboard(request):
    if 'lid' not in request.session:
        return HttpResponse('''<script>alert("You need to login first");window.location="/login/"</script>''')
    
    try:
        student = StudentSignup.objects.get(login_id=request.session['lid'])
    except StudentSignup.DoesNotExist:
        return HttpResponse('''<script>alert("Student not found");window.location="/login/"</script>''')
    
    return render(request, 'student_dashboard.html', {'student': student})

def student_profile(request):
    profile = StudentSignup.objects.get(login_id = request.session['lid'])
    print(request.session['lid'])
    return render (request, 'student_profile.html', {'profile':profile})

from django.shortcuts import render, HttpResponse
from exam_app.models import TeacherSignup

def teacher_dashboard(request):
    if 'lid' not in request.session:
        return HttpResponse('''<script>alert("You need to login first"); window.location="/";</script>''')
    
    try:
        teacher = TeacherSignup.objects.get(login_id=request.session['lid'])
        student_count = StudentSignup.objects.count()
        # Return a response if the teacher exists
        return render(request, 'teacher_dashboard.html', {
            'teacher': teacher,
            'count': student_count
            })
    except TeacherSignup.DoesNotExist:
        # Handle the case where the teacher doesn't exist
        return HttpResponse('''<script>alert("Invalid login details"); window.location="/";</script>''')
    x
def students_list(request):
    student = StudentSignup.objects.all()
    return render (request, 'students_list.html', {'student':student})

def student_edit(request):
    student = StudentSignup.objects.get(login_id=request.session['lid'])
    return render(request, 'student_edit.html',{'student':student})

def student_edit_post(request):
    edit_student = StudentSignup.objects.get(login_id=request.session['lid'])
    print(request.session['lid'])
    edit_student.name = request.POST.get('name', edit_student.name)
    edit_student.clas = request.POST.get('clas', edit_student.clas)
    edit_student.rollno = request.POST.get('rollno', edit_student.rollno)
    edit_student.dob = request.POST.get('dob', edit_student.dob)
    edit_student.username = request.POST.get('username', edit_student.username)
    edit_student.save()
    return HttpResponse('''<script>alert("Edit Successfully");window.location="/student_profile/"</script>''')




def add_exam(request):
    return render (request, 'add_exam.html')

def add_exam_post(request):
    print(request.POST)
    date = request.POST['date']
    title = request.POST['examTitle']
    subject = request.POST['subject']
    ttmark = request.POST['totalMark']
    duration1 = request.POST['duration1']
    duration2 = request.POST['duration2']
    exam = ExamModel(
        date = date,
        title = title,
        subject = subject,
        total_mark = ttmark,
        duration1 = duration1,
        duration2 = duration2,
    )
    exam.save()
    return HttpResponse('''<script>alert("success full");window.location=/upload_exam/</script>''')

def upload_exam(request, exam_id=None):
    if exam_id:
        exam = ExamModel.objects.get(id=exam_id)
        return render(request, 'upload_exam.html', {'exam': exam})
    else:
        exams = ExamModel.objects.all()
        return render(request, 'upload_exam.html', {'exams': exams})

def upload_exam_post(request):
    title = request.POST['title']
    question = request.POST['question']
    option1 = request.POST['option1']
    option2 = request.POST['option2']
    option3 = request.POST['option3']
    option4 = request.POST['option4']
    answer = request.POST['answer']
    
    # Option 1: If you're sending the exam ID in the form, use that instead of title
    # Add a hidden input field with the exam ID in your form
    exam_id = request.POST.get('exam_id')
    if exam_id:
        exam = ExamModel.objects.get(id=exam_id)
    else:
        # Option 2: If you must use title, handle multiple results
        try:
            exam = ExamModel.objects.filter(title=title).first()
            if not exam:
                return HttpResponse("<script>alert('Exam not found!');window.history.back();</script>")
        except Exception as e:
            return HttpResponse(f"<script>alert('Error: {str(e)}');window.history.back();</script>")
    
    questions = QuestionModel(
        exam=exam,
        question=question,
        option1=option1,
        option2=option2,
        option3=option3,
        option4=option4,
        answer=answer,
    )
    questions.save()
    
    # Redirect back to the same exam page
    return HttpResponse(f'''<script>alert("Successfully added question!");window.location="/upload_exam/{exam.id}/";</script>''')

def all_exam(request):
    exam = ExamModel.objects.all()
    return render (request, 'all_exam.html', {'exam':exam})

def todays_exam(request):
    today = timezone.now().date()
    todays_exam = ExamModel.objects.filter(date=today)
    return render (request, 'today_exam.html', {'todays_exam':todays_exam})

def studyMeteriel(request):
    return render (request, 'studyMeteriel.html')