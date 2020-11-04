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

## Start
1. decorators.py里面，初始化
```
activation.initialize(flow_task, None)
```
2. viewflow/flowviews/start.py 里面dispatch
```
self.activation.has_perm(request.user)
self.activation.prepare()
self.dispatch
```
3. django/views/generic/edit.py 里面的post
```
self.object = self.get_object()  # Start.py里面的，直接返回Process
return super().post(request, *args, **kwargs)
```
4. get_object
```
```
5. post
```
form = self.get_form()
if form.is_valid():
    return self.form_valid(form)
```
6. viewflow/flow/views/start.py form_valid
```
super(StartFlowMixin, self).form_valid(*args, **kwargs)
self.activation_done(*args, **kwargs)
return HttpResponseRedirect(self.get_success_url())
```
7. viewflow/flow/views/start.py activation_done
```
self.activation.done()
self.success(_('Process {process} has been started.'))
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
