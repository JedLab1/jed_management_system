from django.contrib import admin
from .models import User, Student

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'created_at', 'updated_at')
    list_filter = ('role', 'created_at')
    search_fields = ('username', 'email')
    ordering = ('-created_at',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'grade', 'enrollment_date', 'profile_completed')
    list_filter = ('grade', 'profile_completed')
    search_fields = ('user__username', 'grade__name') 
    ordering = ('-enrollment_date',)
