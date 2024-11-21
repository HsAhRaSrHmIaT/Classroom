# classroomApp/templatetags/custom_filters.py

from django import template # type: ignore
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def human_readable_date(value):
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    value_date = value.date()

    if value_date == today:
        return f"Today at {value.strftime('%H:%M')}"
    elif value_date == tomorrow:
        return f"Tomorrow at {value.strftime('%H:%M')}"
    else:
        return value.strftime('%A at %H:%M')