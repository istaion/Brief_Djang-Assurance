from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Accède à un élément dans un dictionnaire par sa clé"""
    return dictionary.get(key)