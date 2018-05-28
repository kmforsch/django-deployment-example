from django import template

register = template.Library()
@register.filter(name="cut2")

def cut2(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'two')


# register.filter('cut', cut)
