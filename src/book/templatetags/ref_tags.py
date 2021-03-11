from django.conf import settings
from django.utils.safestring import mark_safe
from django import template


register = template.Library()

@register.simple_tag
def company_name():
    return settings.COMPANY_NAME


# @register.filter
# def strange_summ(book_obj):
#     # book= book_obj.name
#     name = book_obj.name.all()
#     return name

@register.simple_tag
def arrow(td_name, field_to_sort_on, direction_to_sort_on):
    if field_to_sort_on == td_name and direction_to_sort_on == 'up':
        return mark_safe('<i class="fas fa-angle-up"></i>')
    elif field_to_sort_on == td_name and direction_to_sort_on == 'down':
        return mark_safe('<i class="fas fa-angle-down"></i>')          
    return ""
