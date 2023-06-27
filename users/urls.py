from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome,name='welcome'),
    path('student-signup/', views.student_signup,name='student-signup'),
    path('instructor-signup/', views.instructor_signup,name='instructor-signup'),
    path('instructor-signup/', views.instructor_signup,name='instructor-signup'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('404/', views.view404,name='404'),
    path('instructor-dashboard/', views.instructor_dashboard,name='instructor-dashboard'),
    path('student-dashboard/', views.student_dashboard,name='student-dashboard'),
    path('course-detail/<int:pk>/', views.student_course_detail,name='student-coruse-detail'),
    path('profile/', views.profile,name='instructor-profile'),
    path('join-course/', views.join_course,name='join-course'),
    path('schedule/', views.schedule,name='schedule'),
]

