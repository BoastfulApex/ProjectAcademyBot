from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from datetime import datetime


def main(request):
    return render(request, 'main.html')


def courses(request):
    courses = Courses.objects.all()
    courses_passive = []
    courses_active = []
    for i in courses:
        if i.activity:
            if i.end_date < datetime.today().date():
                i.activity = False
                i.save()
                courses_passive.append(i)
            else:
                courses_active.append(i)
        else:
            courses_passive.append(i)
    context = {
        'actives': courses_active,
        'passives': courses_passive,
    }
    return render(request, 'Courses.html', context)


class CoursesCreate(CreateView):
    model = Courses
    fields = '__all__'
    success_url = reverse_lazy('academybot:courses')


class CoursesDelete(DeleteView):
    model = Courses
    fields = '__all__'
    success_url = reverse_lazy('academybot:courses')


def students(request):
    studentes = Student.objects.all()
    payments = Payments.objects.all()
    for student in studentes:
        for payment in payments:
            if student.id == payment.student_id:
                student.total_payment += payment.amount
                student.save()
    context = {
        'students': studentes,
    }
    return render(request, 'students.html', context)


class StudentsCreate(CreateView):
    model = Student
    fields = ['full_name', 'course']
    success_url = reverse_lazy('academybot:students')


def student(request, id):
    student = Student.objects.get(id=id)
    payments = Payments.objects.filter(student_id=id)
    print(payments)
    # pays = []
    # for pay in payments:
    #     if pay.student_id == id:
    #         pays.append(pay)
    course = student.course
    context = {
        'student': student,
        'payments': payments,
        'course': course,
    }
    return render(request, 's_info.html', context=context)


class PaymentsCreate(CreateView):
    model = Payments
    fields = '__all__'
    success_url = reverse_lazy('academybot:students')


def student_by_course(request, id):
    studentes = Student.objects.filter(course_id=id)
    payments = Payments.objects.all()
    for student in studentes:
        for payment in payments:
            if student.id == payment.student_id:
                student.total_payment += payment.amount
                student.save()
    context = {
        'students': studentes,
    }
    return render(request, 'students.html', context)


def course_info(request, pk):
    course = Courses.objects.get(id=pk)
    students = Student.objects.filter(course_id=pk)

    context = {
        'course': course,
        'students': students
    }
    return render(request, 'academybot/course_info.html', context)
