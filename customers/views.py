from django.views.generic import DetailView, ListView

from .models import Person


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person
