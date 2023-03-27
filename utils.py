def logged_events():
    from django.contrib.contenttypes.fields import GenericRelation
    from .models import LogEntryProxy

    return GenericRelation(LogEntryProxy)


def log_event(message, related_object=None, user=None):
    from django.contrib.admin.models import ADDITION, CHANGE, DELETION
    from django.contrib.auth import get_user_model
    from .models import LogEntryProxy

    action_flag = 0
    if any([
        'create' in message.lower(),
        'added' in message.lower(),
        'sent' in message.lower(),
    ]):
        action_flag = ADDITION
    elif any([
        'change' in message.lower(),
        'update' in message.lower(),
        'became' in message.lower(),
        'become' in message.lower(),
        'edit' in message.lower(),
        'approve' in message.lower(),
        'valid' in message.lower(),
    ]):
        action_flag = CHANGE
    elif any([
        'delete' in message.lower(),
        'remove' in message.lower(),
        'cancel' in message.lower(),
    ]):
        action_flag = DELETION

    if not user:
        User = get_user_model()
        user = User.objects.filter(pk=1).first()

    if user:
        LogEntryProxy.objects.create(
            user=user,
            content_object=related_object,
            object_repr=str(related_object)[:200] if related_object else '',
            action_flag=action_flag,
            change_message=message,
        )