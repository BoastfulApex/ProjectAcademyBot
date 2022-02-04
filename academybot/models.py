from django.db import models


class Courses(models.Model):
    course_name = models.CharField(max_length=250, null=True)
    course_price = models.IntegerField()
    begin_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    activity = models.BooleanField(default=True)

    @property
    def is_active(self):
        return self.activity

    def __str__(self):
        return self.course_name


class Student(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    total_payment = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


class Payments(models.Model):
    amount = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    payment_data = models.DateField(auto_now_add=True)
