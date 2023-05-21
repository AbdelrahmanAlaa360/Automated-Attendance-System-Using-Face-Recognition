from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.course_create_view,name='create-course'),
    path('detail/<int:pk>/',views.CourseDetailView.as_view(),name='course-detail'),
    path('lecture-detail/<int:pk>/',views.LectureDetailView.as_view(),name='lecture-detail'),
    path('start-model/',views.start_model,name='start-model'),
]
