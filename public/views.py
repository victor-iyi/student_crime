from django.shortcuts import render
from django.views.generic import ListView

from students.models import Student


# Create your views here.
class HomePage(ListView):
    template_name = 'public/index.html'

    def get_queryset(self):
        return Student.objects.all()


def about(request):
    return render(request, 'public/about.html')
