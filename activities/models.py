from django.db import models
from django.utils import timezone
from academics.models import Chapter,Method
from users.models import Student


# ActivityTypes model
class ActivityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DifficultyLevel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ActivityModel(models.Model):
    id = models.AutoField(primary_key=True)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default='')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)  # Assuming a 'Chapters' model exists
    theoretical_text = models.TextField(null=True, blank=True)
    questions_list = models.JSONField(null=True, blank=True)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    items = models.JSONField(null=True, blank=True)  # Field to store item names with their SVGs


    def __str__(self):
        return f"{self.activity_type} - {self.name}"
    def get_item_svg(self, item_name):
        # Assuming 'items' is a JSONField with a dictionary of item names and SVGs
        item = self.items.get(item_name)
        return item['svg_content'] if item else None
    
# ActivityInstances model
class ActivityInstance(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Assuming a 'Students' model exists
    activity_model = models.ForeignKey(ActivityModel, on_delete=models.CASCADE)
    result = models.CharField(max_length=50)
    attempted_at = models.DateTimeField(default=timezone.now)
    unique_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.activity_model.activity_type} - {self.activity_model.chapter} - Student {self.student.user}"


# PainPoints model
class PainPoint(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    PAIN_LEVEL_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Assuming a 'Students' model exists
    method = models.ForeignKey(Method, on_delete=models.CASCADE)  # Assuming a 'Methods' model exists
    aspect_name = models.CharField(max_length=100)
    pain_level = models.CharField(max_length=6, choices=PAIN_LEVEL_CHOICES)
    activity_instance = models.ForeignKey(ActivityInstance, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f" {self.method}- Student {self.student.user} - {self.aspect_name}"
