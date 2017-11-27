from django.views.generic import ListView, DetailView

from .models import Suspects


# /suspects
class SuspectsAll(ListView):
    template_name = 'suspects/index.html'
    context_object_name = 'suspects'

    def get_queryset(self):
        return Suspects.objects.all()


# /suspects/12
class SuspectsDetail(DetailView):
    template_name = 'suspects/detail.html'
    pk_url_kwarg = 'suspect_id'
    model = Suspects
