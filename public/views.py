from django.shortcuts import render
from django.views.generic import ListView

from suspects.models import Suspect


# Create your views here.
class HomePage(ListView):
    template_name = 'public/index.html'
    context_object_name = 'suspects'

    def get_queryset(self):
        return Suspect.objects.all()


def about(request):
    return render(request, 'public/about.html')
