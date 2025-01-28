from django import template
from datetime import datetime

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Accède à un élément dans un dictionnaire par sa clé"""
    return dictionary.get(key)

@register.filter
def availability_for_day_hour(availabilities, date_hour):
    date, hour = date_hour.split('|')
    for availability in availabilities:
        # Convertir les disponibilités pour comparer avec la date et l'heure
        if availability.day_of_week == datetime.strptime(date, "%Y-%m-%d").weekday():
            start_time = availability.start_time.strftime("%H:%M")
            end_time = availability.end_time.strftime("%H:%M")
            if start_time <= hour < end_time:
                return True
    return False