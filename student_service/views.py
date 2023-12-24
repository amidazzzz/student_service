from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Grade
from django.db.models import Avg

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def add_grade(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        subject = request.POST['subject']
        value = request.POST['value']
        Grade.objects.create(student=student, subject=subject, value=value)
        return redirect('student_detail', student_id=student_id)

    return render(request, 'add_grade.html', {'student': student})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    grades = Grade.objects.filter(student=student)
    average_grade = grades.aggregate(Avg('value'))['value__avg']
    return render(request, 'student_detail.html', {'student': student, 'grades': grades, 'average_grade': average_grade})

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        student = Student.objects.create(first_name=first_name, last_name=last_name)
        return render(request, 'student_detail.html', {'student': student})
    else:
        return render(request, 'student_form.html')
