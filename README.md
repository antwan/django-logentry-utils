Django Admin LogEntry utilities
===============================

This is a small collection of utilities to enhance [Django Admin's `LogEntry` model](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#logentry-objects) so it can be leveraged to log and view events happening outside of Django Admin.


Installation
------------

- Import the classes in your code
- Optionnal: Inherit serializers from `ChangeLoggerMixin` so all user modifications (PATCH) are logged automatically
- Optionnal: Add `logged_events` queryset manager to your models so you can access log entries conveniently


Usage
-----

### Logging entries

```
from .utils import log_event

# ...

# Object changed with no link to a user
my_object=Class.object.get(pk=1)
my_object.status = False
my_object.save()
log_event(my_object, 'Status became false')


# Object changed because of a user action
def change_value_view(self):
    value = self.request.POST.get('value')
    my_object=Class.object.get(pk=self.request.POST.get('id'))
    my_object.value = value
    my_object.save()
    log_event(my_object, 'Value changed to' + value, self.request.user)
```

### Accessing log entries

```
from utils import logged_events

class MyClass(models):
    # fields
    logged_events = logged_events()
```

```
my_object=Class.object.get(pk=1)
my_object.logged_events.filter(create_gte=now()-timedelta(days=7))
# prints all events from last week attached to the object
```




