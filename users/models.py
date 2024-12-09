from django.db import models
from django.utils import timezone
from academics.models import Grade
# Users model
class User(models.Model):
    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


# Students model
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=timezone.now)
    profile_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.grade}"

