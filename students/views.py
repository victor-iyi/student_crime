from django.views.generic import ListView, DetailView

from .models import Student


# /students
class Index(ListView):
    template_name = 'students/index.html'

    def get_queryset(self):
        return Student.objects.all()


# /students/39
class Detail(DetailView):
    template_name = 'students/detail.html'
    pk_url_kwarg = 'student_id'
    model = Student
