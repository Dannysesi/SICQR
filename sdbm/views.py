# students/views.py
from django.shortcuts import render, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'first.html', {'student': student})

