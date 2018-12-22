# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('blogging_for_humans.urls', namespace='blogging_for_humans')),
]
