from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import datetime

from django.contrib.auth.models import User

class Login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

class StudentSignup(models.Model):
    name = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/', null=True, blank=True) 
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class TeacherSignup(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=[('social', 'Social'), ('biology', 'Biology'), ('maths', 'Maths')])
    phonenumber = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.FileField(upload_to='media/', null=True, blank=True) 
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    
class ExamModel(models.Model):
    date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    total_mark = models.IntegerField()
    duration1 = models.CharField(max_length=50)
    duration2 = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class QuestionModel(models.Model):
    OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]

    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=150)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, choices=OPTION_CHOICES)

    def __str__(self):
        return self.question
    
    
    
    
    
    
class StudentAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the logged-in student
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)  # Link to the question
    submitted_answer = models.CharField(max_length=1)  # Store the submitted answer (a, b, c, d)
    is_correct = models.BooleanField(default=False)  # Indicates if the answer is correct

    def __str__(self):
        return f"{self.student.username} - {self.question.question}"
    
    
    
class ExamResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the logged-in student
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)  # Link to the exam
    score = models.IntegerField()  # Store the total score
    total_questions = models.IntegerField()  # Store the total number of questions
    percentage_score = models.FloatField()  # Store the percentage score
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp of submission

    def __str__(self):
        return f"{self.student.username} - {self.exam.title} - {self.percentage_score}%"