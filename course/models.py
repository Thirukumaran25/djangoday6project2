from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title=models.CharField()
    description=models.CharField()
    teachers=models.ManyToManyField(Teacher, related_name='courses')

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    title=models.CharField()
    content=models.TextField()
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name= 'lessons')