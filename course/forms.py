from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'sessionHour', 'sessionDay', 'type', 'seessionTime', 'capturingTime', 'sessionPlace', 'totalNumberOfLectures']
        
