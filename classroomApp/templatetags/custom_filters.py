# classroomApp/templatetags/custom_filters.py

from django import template # type: ignore
from datetime import timedelta, datetime
from django.utils import timezone # type: ignore
from django.utils.timesince import timesince # type: ignore

register = template.Library()
@register.filter
def human_readable_date(value):
    # Check if the value is a string and convert it to a datetime object
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value)
        except ValueError:
            return value  # Return the original value if it cannot be parsed

    # Ensure the datetime object is timezone-aware
    if not timezone.is_aware(value):
        value = timezone.make_aware(value)

    # Convert the datetime object to the current timezone
    value = timezone.localtime(value)
    # Check if the time difference is more than 24 hours
    time_difference = timezone.now() - value
    if time_difference.days > 1:
        return value.strftime('%a')
    elif time_difference.days == 1:
        return "yesterday"
    elif time_difference.seconds >= 3600:
        return "today at " + value.astimezone(timezone.get_current_timezone()).strftime('%I:%M %p')
    elif time_difference.seconds >= 60:
        return str(time_difference.seconds // 60) + " minutes ago"
    else:
        return "just now"