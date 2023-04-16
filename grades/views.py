from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student

def studentsList(request):
    all_students_list = Student.objects.all()
    template = loader.get_template("grades/studentsList.html")
    context = {
        "all_students_list": all_students_list,
    }
    return HttpResponse(template.render(context, request))


def studentSubjects(request, student_id=None):
    return HttpResponse(f"this are the student {student_id} subjects" )

def subjectAssignments(request, student_id, subject_id, grades_id=None):
    return HttpResponse(f"this is {subject_id} assignments {grades_id} of {student_id} ")



# Create your views here.
