from django.shortcuts import render
from django.views.generic import ListView

from students.models import Student


# Create your views here.
class HomePage(ListView):
    template_name = 'public/index.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all()[:20:-1]


def about(request):
    return render(request, 'public/about.html')
