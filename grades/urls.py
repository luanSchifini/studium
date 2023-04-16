from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.studentsList, name="students list"),
    # ex: /polls/5/
    path("<int:student_id>/student_subjects/", views.studentSubjects, name="subjects"),
    path("<int:subject_id>/subject_assignments/", views.subjectAssignments, name="student assignment grades")
]

