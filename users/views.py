from django.shortcuts import render,redirect ,get_object_or_404
from .forms import UserRegisterForm,CustomAuthenticationForm,ProfileImageForm,TrainingImageForm
from datetime import datetime, time
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from  .models import User , ProfileImage,TrainImage
from course.models import Course,Lecture
from django.views.generic import (
    DetailView,
)

def welcome(request):
    return render(request,'welcome.html')

def student_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.instance.is_student=True
            form.save()
            ProfileImage.objects.create(user=form.instance)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/student_signup.html', {'form': form})

def instructor_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.instance.is_teacher=True
            form.save()
            ProfileImage.objects.create(user=form.instance)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/instructor_signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_student:
                return redirect('student-dashboard')
            else:
                return redirect('instructor-dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')



def view404(request):
    return render(request,'404page.html')




@user_passes_test(lambda u: u.is_authenticated and u.is_teacher,login_url='404')
def instructor_dashboard(request):
    courses = Course.objects.filter(id__in=request.user.courses.values_list('id', flat=True))
    print(courses)
    lectures=[]
    for course in courses:
        for lecture in course.lecture.all():
            lectures.append(lecture)
    sorted_lectures = sorted(lectures, key=lambda x: x.data)
    first_three_lectures = sorted_lectures[:3]
    context={'courses' : courses}
    context['lectures']=first_three_lectures
    return render(request,'instructor/dashboard.html' ,context)

@user_passes_test(lambda u: u.is_authenticated and u.is_student,login_url='404')
def student_dashboard(request):

    context={}
    courses = Course.objects.filter(id__in=request.user.courses.values_list('id', flat=True))
    lectures=[]
    for course in courses:
        for lecture in course.lecture.all():
            lectures.append(lecture)
    total_sessions=len(lectures)
    attended=0
    absent=0
    for lecture in lectures:
        if request.user in lecture.user.all():
            attended +=1
        else:
            absent+=1
    sorted_lectures = sorted(lectures, key=lambda x: x.data)
    lecture_names=[]
    lecture_course=[]
    lecture_date=[]
    lecture_type=[]
    lecture_status=[]
    for lecture in sorted_lectures:
        lecture_names.append(lecture.name)
        lecture_course.append(lecture.course.name)
        lecture_date.append(lecture.data)
        lecture_type.append("fix me")
        lecture_status.append(request.user in lecture.user.all())
    context['lecture_names']=lecture_names
    context['lecture_course']=lecture_course
    context['lecture_date']=lecture_date
    context['lecture_type']=lecture_type
    context['lecture_status']=lecture_status
    context['courses']=courses
    context['attended']=attended
    context['total_sessions']=total_sessions
    context['absent']=absent
    return render(request,'student/index.html' , context)

@user_passes_test(lambda u: u.is_authenticated and u.is_student,login_url='404')
def student_course_detail(request,pk):
    course = get_object_or_404(Course, id=pk)
    courses = Course.objects.filter(id__in=request.user.courses.values_list('id', flat=True))
    lectures=[]
    for lecture in course.lecture.all():
        lectures.append(lecture)
    total_sessions=len(lectures)
    attended=0
    absent=0
    for lecture in lectures:
        if request.user in lecture.user.all():
            attended +=1
        else:
            absent+=1
    sorted_lectures = sorted(lectures, key=lambda x: x.data)
    context={}
    context['courses']=courses
    context['course']=course
    context['attended']=attended
    context['total_sessions']=total_sessions
    context['absent']=absent
    context['lectures']=sorted_lectures
    return render(request,'student/course.html' ,context)


@user_passes_test(lambda u: u.is_authenticated ,login_url='404')
def profile(request):

    user = request.user
    profileImage = user.profile

    if request.method == 'POST':

        updateImageForm = ProfileImageForm(request.POST, request.FILES)
        trainingForm = TrainingImageForm(request.POST, request.FILES)

        if updateImageForm.is_valid():
            profileImage.image = updateImageForm.cleaned_data['image']
            profileImage.save()
            return redirect('instructor-profile')
        if trainingForm.is_valid():
            for image in request.FILES.getlist('images'):
                TrainImage.objects.create(user=user, image=image)
            return redirect('instructor-profile')
    else:
        updateImageForm = ProfileImageForm()
        trainingForm = TrainingImageForm()

    return render(request, 'instructor/profile.html', {'profileImageForm': updateImageForm ,'trainingForm':trainingForm})

@user_passes_test(lambda u: u.is_authenticated and u.is_student,login_url='404')
def join_course(request):
    if request.method=='POST':

        code=request.POST.get('code')
        if code:
            course=get_object_or_404(Course,code=code)
            request.user.courses.add(course)
        return redirect('student-dashboard')
    return render(request,'student/index.html')


def schedule(request):

    time_intervals = {
    'Sunday': {
        1: {'name': 'place'},
        2: {'name': 'place'},
        3: {'name': 'place'},
        4: {'name': 'place'},
        5: {'name': 'place'},
    },
    'Monday': {
        1: {'name': 'place'},
        2: {'name': 'place'},
        3: {'name': 'place'},
        4: {'name': 'place'},
        5: {'name': 'place'},
    },
    'Tuesday': {
        1: {'name': 'place'},
        2: {'name': 'place'},
        3: {'name': 'place'},
        4: {'name': 'place'},
        5: {'name': 'place'},
    },
    'Wednesday': {
        1: {'name': 'place'},
        2: {'name': 'place'},
        3: {'name': 'place'},
        4: {'name': 'place'},
        5: {'name': 'place'},
    },
    'Thursday': {
        1: {'name': 'place'},
        2: {'name': 'place'},
        3: {'name': 'place'},
        4: {'name': 'place'},
        5: {'name': 'place'},
    }
}

    courses = Course.objects.filter(id__in=request.user.courses.values_list('id', flat=True))
    eight_am = time(8, 0)  
    ten_am = time(10, 0)  
    twelve_pm = time(12, 0)  
    two_pm = time(14, 0)  
    four_pm = time(16, 0)  

    for course in courses:
        course_day=course.sessionDay
        course_time=course.seessionTime
        if course_time==eight_am:
            time_intervals[course_day][1]['name']=course.name
            time_intervals[course_day][1]['place']=course.sessionPlace
        elif course_time==ten_am:
            time_intervals[course_day][2]['name']=course.name
            time_intervals[course_day][2]['place']=course.sessionPlace
        elif course_time==twelve_pm:
            time_intervals[course_day][3]['name']=course.name
            time_intervals[course_day][3]['place']=course.sessionPlace
        elif course_time==two_pm:
            time_intervals[course_day][4]['name']=course.name
            time_intervals[course_day][4]['place']=course.sessionPlace
        else:
            time_intervals[course_day][5]['name']=course.name
            time_intervals[course_day][5]['place']=course.sessionPlace
    return render(request,'student/schedule.html',{'coursesTime':time_intervals})