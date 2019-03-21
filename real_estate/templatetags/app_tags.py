from django import template
from django.template.defaultfilters import slugify

from ..utils import *
register = template.Library()


@register.simple_tag
def slugify_tag(text):
    """
    This function will remove accents of vietnamese word.
    Also, It will generate human-readable url
    """
    removed_str = remove_accents(text)
    return slugify(removed_str)
