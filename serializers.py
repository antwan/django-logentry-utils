class ChangeLoggerMixin(object):
    def update(self, instance, validated_data):
        change_messages = []
        for field, value in validated_data.items():
            old_value = getattr(instance, field)
            if old_value != value:
                change_messages.append('Changed "{}" from "{}" to "{}"'.format(field, old_value, value))
        try:
            ret = super(ChangeLoggerMixin, self).update(instance, validated_data)
        except NotImplementedError:
            ret = None
        if change_messages:
            log_event(
                ', '.join(change_messages),
                instance,
                self.context['request'].user if self.context and self.context.get('request') else None
            )
        return ret