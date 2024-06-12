from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentAddForm
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'base.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'first.html', {'student': student})

@login_required(login_url='/login')
def add_student(request):
    student = Student.objects.all()
    if request.method =='POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail/')
    else:
        form = StudentAddForm()

    return render(request, 'addstudent.html', {'form': form})