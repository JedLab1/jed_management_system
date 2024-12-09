from django.db import models

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name    
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.grade.name} - {self.name}"

class Method(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Aspect(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name   
    
