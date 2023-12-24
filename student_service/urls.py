from django.urls import path
from .views import student_list, student_detail, add_student, add_grade

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
    path('add_student/', add_student, name='add_student'),
    path('add_grade/<int:student_id>/', add_grade, name='add_grade'),

]
