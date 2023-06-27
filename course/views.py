from django.shortcuts import render,redirect
from .forms import CourseForm
from .models import Course,Lecture
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from users.models import User
import subprocess
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

@user_passes_test(lambda u: u.is_authenticated and u.is_teacher,login_url='404')
def course_create_view(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.instance.save()
            form.instance.user.add(request.user)
            course_id = form.instance.id
            print("Created course ID:", course_id)
            return redirect('instructor-dashboard')
    else:
        form=CourseForm()
    return render(request, 'course/courseForm.html', {'form':form})

@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_teacher, login_url='404'),name='dispatch')
class CourseDetailView(DetailView):
    model=Course

@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_teacher, login_url='404'),name='dispatch')
class LectureDetailView(DetailView):
    model=Lecture

@user_passes_test(lambda u: u.is_authenticated and u.is_teacher,login_url='404')
def start_model(request, id):
    #command = ['python', 'E:/GP github/automation-face-attendance/model/face_detect.py']
    command = ['python', 'D:/Projects/Automated-Attendance-System-Using-Face-Recognition/model/face_detect.py']
    subprocess.run(command)
    course = Course.objects.get(id = id)
    with open('D:/Projects/Automated-Attendance-System-Using-Face-Recognition/attendance.txt', 'r') as file:
        lines = file.readlines()
        users = []
        for line in lines:
            if line[-1] == '\n':
                line = line.rstrip('\n')
            if(line == "Unknown"):
                continue
            else:
                user = User.objects.get(username = line)
                users.append(user)
    lecture = Lecture.objects.create(name = "Lecture" , course = course)
    lecture.user.set(users)
    print(course)
    return render(request,'course/modlePage.html')