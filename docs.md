**Xiang Wang @ 2020-11-03 13:12:10**

# Concept
## Flow

# Node
## Event(Node)
```
"""Base class for event-based tasks."""
```

## Start(Event)

## Task(Node)
```
"""Base class for tasks."""
```

## BaseView(Task)
## View(BaseView)
```
approve = flow.View(UpdateProcessView)
```

# How it works
```
Flow.urls:
    for node in self._meta.nodes():
        node_urls += node.urls()
```

```
BaseView.urls
    re_path(
        r'^(?P<process_pk>\d+)/{}/(?P<task_pk>\d+)/$'.format(self.name),
        self.view, {'flow_task': self}, name=self.name
    )
DetailViewMixin
    def urls(self):
        return urls.append(
            url(process_pk/name/task_pk/detail/), self.detail_view
        )
UpdateProcessView(FlowMixin, django.generic.UpdateView):
FlowMixin:
    def form_valid(self):
        self.activation.done()
```

# Logic
```
IfActivation
    def activate_next(self):
        if self.condition_result
            self.flow_task._on_true.activate()
        else:
            self.flow_task._on_false.activate()
```
