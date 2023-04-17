from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.students_list, name="students list"),
    # ex: /polls/5/
    path("<int:student_id>/student_subjects/", views.student_subjects, name="subjects"),
    path("<int:subject_id>/subject_assignments/", views.subject_assignments, name="student assignment grades")
]

