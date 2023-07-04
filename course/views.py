from django.shortcuts import render,redirect
from .forms import CourseForm
from .models import Course,Lecture
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from users.models import User
from django.urls import reverse,reverse_lazy
import subprocess
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
    command = ['python', 'E:/GP github/v2/automation-face-attendance/model/face_detect.py']
    #command = ['python', 'D:/Projects/Automated-Attendance-System-Using-Face-Recognition/model/face_detect.py']
    subprocess.run(command)
    course = Course.objects.get(id = id)
    #with open('D:/Projects/Automated-Attendance-System-Using-Face-Recognition/attendance.txt', 'r') as file:
    with open('E:/GP github/v2/automation-face-attendance/attendance.txt', 'r') as file:
        lines = file.readlines()
        users = []
        for line in lines:
            if line[-1] == '\n':
                line = line.rstrip('\n')
            if(line == "Unknown"):
                continue
            else:
                user = User.objects.get(username = line)
                if user in course.user.all():
                    users.append(user)
    lecture = Lecture.objects.create(name = "Lecture" , course = course)
    lecture.user.set(users)
    lecture_pk=lecture.id 
    print(course)
    url = reverse('lecture-detail', args=[lecture_pk])
    return redirect(url)

class UpdateCourseView(UpdateView):
    model = Course
    fields = ['name', 'sessionHour', 'sessionDay', 'type', 'seessionTime',
              'capturingTime', 'sessionPlace', 'totalNumberOfLectures']
    template_name = 'course/course_update.html'
    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.object.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['helper'] = self.get_form_helper()
        return context

    def get_form_helper(self):
        helper = FormHelper()
        helper.form_method = 'post'
        helper.add_input(Submit('submit', 'Update Course'))
        helper.form_class = 'form-horizontal'
        helper.label_class = 'col-lg-20'
        helper.field_class = 'col-lg-10'
        return helper