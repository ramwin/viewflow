#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2020-11-03 11:39:17

from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import HelloWorldProcess
from .views import HelloWorldViewSet


class HelloWorldFlow(Flow):
    process_class = HelloWorldProcess

    start = (
        flow.Start(
            HelloWorldViewSet.as_view({'post':'create'}),
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_hello_world_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_hello_world_request(self, activation):
        print(activation.process.text)
