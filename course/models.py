from django.db import models
from users.models import User
from datetime import datetime

class Course(models.Model):
    TYPE_CHOICES=[
            ('lecture','lecture')
            ,('section','section')
        ]
    
    DAYS_CHOICES = [
            ('mon', 'Monday'),
            ('tue', 'Tuesday'),
            ('wed', 'Wednesday'),
            ('thu', 'Thursday'),
            ('fri', 'Friday'),
            ('sat', 'Saturday'),
            ('sun', 'Sunday'),
        ]
    
    name=models.CharField(max_length=255)
    sessionHour=models.IntegerField(default=2)
    sessionDay=models.CharField(max_length=10,choices=DAYS_CHOICES,default='Sunday')
    type=models.CharField(max_length=10,choices=TYPE_CHOICES,default='lecture')
    seessionTime=models.TimeField(default=datetime.now)
    capturingTime=models.IntegerField(default=30)
    sessionPlace=models.CharField(max_length=10,null=True)
    totalNumberOfLectures=models.IntegerField(default=13)
    user=models.ManyToManyField(User,related_name='courses')

    def __str__(self):
        return self.name
    
class Lecture(models.Model):
    name=models.CharField(max_length=255)
    data=models.DateField()
    type=models.CharField(max_length=255,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True,related_name='lecture')
    user=models.ManyToManyField(User,related_name='lecture',blank=True)
    def __str__(self):
        return self.name