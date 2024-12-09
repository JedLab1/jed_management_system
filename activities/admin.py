from django.contrib import admin
from .models import ActivityType, DifficultyLevel, ActivityModel, ActivityInstance, PainPoint

@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(DifficultyLevel)
class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(ActivityModel)
class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_type', 'chapter')
    list_filter = ('activity_type', 'difficulty_level', 'chapter')
    search_fields = ('activity_type__name', 'chapter__name')  # Assuming Chapter model has a 'name' field
    ordering = ('-created_at',)


@admin.register(ActivityInstance)
class ActivityInstanceAdmin(admin.ModelAdmin):
    list_display = ('activity_model', 'student', 'result', 'attempted_at')
    list_filter = ('activity_model', 'result')
    search_fields = ('activity_model__activity_type__name', 'student__user__username')  # Assuming Student model links to User with 'username'
    ordering = ('-attempted_at',)


@admin.register(PainPoint)
class PainPointAdmin(admin.ModelAdmin):
    list_display = ('student', 'method', 'aspect_name', 'pain_level', 'created_at')
    list_filter = ('pain_level', 'method')
    search_fields = ('aspect_name', 'student__user__username')  # Assuming Student model links to User with 'username'
    ordering = ('-created_at',)
