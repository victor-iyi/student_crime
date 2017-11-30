from django.views.generic import ListView, DetailView

from suspects.models import Suspect


class Index(ListView):
    template_name = 'suspects/index.html'

    def get_queryset(self):
        return Suspect.objects.all()


class Detail(DetailView):
    template_name = 'suspects/detail.html'
    pk_url_kwarg = 'suspect_id'
    model = Suspect
