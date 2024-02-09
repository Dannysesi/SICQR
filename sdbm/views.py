from django.shortcuts import render, get_object_or_404
from .models import Student


def base(request):
    return render(request, 'base.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'first.html', {'student': student})

