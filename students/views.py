from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView

from students.models import Student


# /students
class Index(ListView):
    template_name = 'students/index.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all()


# /students/39
class Detail(DetailView):
    template_name = 'students/detail.html'
    pk_url_kwarg = 'student_id'
    model = Student

"""
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
