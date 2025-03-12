from django.db import models
from django.contrib.auth.hashers import make_password, check_password

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
    login = models.ForeignKey(Login, on_delete=models.CASCADE)

class TeacherSignup(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=[('social', 'Social'), ('biology', 'Biology'), ('maths', 'Maths')])
    phonenumber = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login = models.ForeignKey(Login, on_delete=models.CASCADE)