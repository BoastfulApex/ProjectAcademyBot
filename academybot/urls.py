from django.urls import path
from .views import *

app_name = 'academybot'

urlpatterns = [
    path('', main, name='home'),
    path('courses/', courses, name='courses'),
    path('course/<int:pk>', course_info, name='course_info'),
    path('course_add/', CoursesCreate.as_view(), name='course_add'),
    path('delete/<int:pk>', CoursesDelete.as_view(), name='delete'),
    path('students/', students, name="students"),
    path('students/<int:id>', student, name="student_info"),
    path('course/<int:id>', student_by_course, name="student_by_course"),
    path('students_add/', StudentsCreate.as_view(), name="students_add"),
    path('payment_add/', PaymentsCreate.as_view(), name="payment_add"),
]
