from django.views.generic import ListView, DetailView

from .models import Students


# /students
class StudentsAll(ListView):
    template_name = 'students/index.html'

    def get_queryset(self):
        return Students.objects.all()


# /students/39
class StudentDetail(DetailView):
    template_name = 'students/detail.html'
    pk_url_kwarg = 'student_id'
    model = Students
