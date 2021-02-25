from django import template


register = template.Library()


@register.filter(name="device_type_printer")
def device_type_printer(obj):
    return obj.device_type_printer()
