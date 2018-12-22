# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'blogging_for_humans'
urlpatterns = [
    url(
        regex="^Scoop/~create/$",
        view=views.ScoopCreateView.as_view(),
        name='Scoop_create',
    ),
    url(
        regex="^Scoop/(?P<pk>\d+)/~delete/$",
        view=views.ScoopDeleteView.as_view(),
        name='Scoop_delete',
    ),
    url(
        regex="^Scoop/(?P<pk>\d+)/$",
        view=views.ScoopDetailView.as_view(),
        name='Scoop_detail',
    ),
    url(
        regex="^Scoop/(?P<pk>\d+)/~update/$",
        view=views.ScoopUpdateView.as_view(),
        name='Scoop_update',
    ),
    url(
        regex="^Scoop/$",
        view=views.ScoopListView.as_view(),
        name='Scoop_list',
    ),
	url(
        regex="^Flavor/~create/$",
        view=views.FlavorCreateView.as_view(),
        name='Flavor_create',
    ),
    url(
        regex="^Flavor/(?P<pk>\d+)/~delete/$",
        view=views.FlavorDeleteView.as_view(),
        name='Flavor_delete',
    ),
    url(
        regex="^Flavor/(?P<pk>\d+)/$",
        view=views.FlavorDetailView.as_view(),
        name='Flavor_detail',
    ),
    url(
        regex="^Flavor/(?P<pk>\d+)/~update/$",
        view=views.FlavorUpdateView.as_view(),
        name='Flavor_update',
    ),
    url(
        regex="^Flavor/$",
        view=views.FlavorListView.as_view(),
        name='Flavor_list',
    ),
	]
