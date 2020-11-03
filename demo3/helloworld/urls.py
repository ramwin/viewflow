#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-11-03 11:41:38


from viewflow.flow.viewset import FlowViewSet
from django.urls import path, include
from .flows import HelloWorldFlow


urlpatterns = [
    path('testflow/', include(
        FlowViewSet(HelloWorldFlow).urls
    )),
]
