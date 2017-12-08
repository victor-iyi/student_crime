from django.contrib.messages.views import SuccessMessageMixin
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
    pk_url_kwarg = 'student_id'
    model = Student


class StudentCreate(CreateView, SuccessMessageMixin):
    template_name = 'students/register.html'
    model = Student
    fields = ['name', 'matric', 'gender', 'level', 'department', 'image']
    success_url = '/students/'
    success_message = '%(name) with matric number %(matric) was successfully created!'


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'matric', 'gender', 'level', 'department', 'image']


class StudentDelete(DeleteView, SuccessMessageMixin):
    model = Student
    success_url = reverse_lazy('students:index')
    success_message = '%(name)s was successfully deleted!'


"""
from django.shortcuts import render_to_response
from django.template import RequestContext

def e_handle404(request):
    context = RequestContext(request)
    response = render_to_response('404.html', context)
    response.status_code = 404
    return response


def e_handle500(request):
    context = RequestContext(request)
    response = render_to_response('500.html', context)
    response.status_code = 500
    return response
"""
