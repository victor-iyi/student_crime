from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student


# /students
class Index(ListView):
    template_name = 'students/index.html'
    __col_name = 'department'
    context_object_name = __col_name

    def get_queryset(self):
        cols = Student.objects.values_list(self.__col_name, flat=True)
        return [Student.objects.filter(department=col) for col in set(cols)]


# /students/39
class Detail(DetailView):
    template_name = 'students/detail.html'
    model = Student


# /students/register
class StudentCreate(CreateView):
    template_name = 'students/register.html'
    model = Student
    fields = ['name', 'matric', 'gender', 'level', 'department', 'image']


# /students/update/39
class StudentUpdate(UpdateView):
    template_name = 'students/update.html'
    model = Student
    # fields = ['name', 'matric', 'gender', 'level', 'department', 'image']


# /students/delete/39
class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students:index')
