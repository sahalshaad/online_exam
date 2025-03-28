from django.contrib import admin
from .models import *
# Register your models here.  pswrd: onlineExm
class Logins(admin.ModelAdmin):
    list_display = ["username", "password", "type"]
    readonly_fields = ["password"]
admin.site.register(Login, Logins)

class Students(admin.ModelAdmin):
    list_display = ['name', 'clas', 'rollno', 'dob', 'username']
    readonly_fields = ['password']
admin.site.register(StudentSignup, Students)

class Trachers(admin.ModelAdmin):
    list_display = ['name', 'department', 'phonenumber', 'username']
    readonly_fields = ['password']
admin.site.register(TeacherSignup, Trachers)
