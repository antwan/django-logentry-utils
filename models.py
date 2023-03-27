from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.fields import GenericForeignKey


class LogEntryProxy(LogEntry):
    """
    This is a wrapper around LogEntry with slightly improved usability
    - Cleaner representation of objects in the console
    - Possibility to get/set a generic related `content_object` directly without passing manually the ID and content type
    """

    content_object = GenericForeignKey()

    @property
    def created(self):
        return self.action_time

    @property
    def message(self):
        return self.change_message

    def __repr__(self):
        return self.__unicode__()

    def __str__(self):
        return '[{}] {}'.format(self.created, self.message)

    class Meta:
        proxy = True