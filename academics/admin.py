from django.contrib import admin
from .models import Subject, Chapter, Method,Grade

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display id and name in the list view
    search_fields = ('name',)  # Enable search by name
    ordering = ('name',)  # Order by name in ascending order

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Display id and name in the list view
    search_fields = ('name',)  # Enable search by name
    ordering = ('name',)  # Order by name in ascending order


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'grade', 'created_at')
    list_filter = ('subject', 'grade', 'created_at')  # Add filters for subject, grade level, and creation date
    search_fields = ('name', 'subject__name')  # Enable search by chapter name and subject name
    ordering = ('-created_at',)  # Order by creation date in descending order

@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chapter', 'created_at')
    list_filter = ('chapter', 'created_at')  # Add filters for chapter and creation date
    search_fields = ('name', 'chapter__name')  # Enable search by method name and chapter name
    ordering = ('-created_at',)  # Order by creation date in descending order


