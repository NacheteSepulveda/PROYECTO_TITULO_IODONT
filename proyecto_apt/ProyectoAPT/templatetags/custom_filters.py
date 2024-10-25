from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    """Return the value for key in dictionary d, or None if key is not found."""
    return d.get(key, None)  # Retorna None si no se encuentra la clave

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
