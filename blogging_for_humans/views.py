# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Scoop,
	Flavor,
)


class ScoopCreateView(CreateView):

    model = Scoop


class ScoopDeleteView(DeleteView):

    model = Scoop


class ScoopDetailView(DetailView):

    model = Scoop


class ScoopUpdateView(UpdateView):

    model = Scoop


class ScoopListView(ListView):

    model = Scoop


class FlavorCreateView(CreateView):

    model = Flavor


class FlavorDeleteView(DeleteView):

    model = Flavor


class FlavorDetailView(DetailView):

    model = Flavor


class FlavorUpdateView(UpdateView):

    model = Flavor


class FlavorListView(ListView):

    model = Flavor

