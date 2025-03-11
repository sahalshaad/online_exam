from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Login"
        verbose_name_plural = "Logins"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"
    
class student_signup(models.Model):
    name = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    login = models.ForeignKey(login, on_delete=models.CASCADE)