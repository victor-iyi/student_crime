from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Students, Suspects


# Create your views here.
def index(request):
    return render(request, template_name='students/index.html')


# /all
class StudentsAll(ListView):
    template_name = 'students/all.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Students.objects.all()


# /student/39
class StudentDetail(DetailView):
    template_name = 'students/student-detail.html'
    pk_url_kwarg = 'student_id'
    model = Students


# /suspects
class SuspectsAll(ListView):
    template_name = 'students/suspects.html'
    context_object_name = 'suspects'

    def get_queryset(self):
        return Suspects.objects.all()


