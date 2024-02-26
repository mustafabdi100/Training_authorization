from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Adds a CSS class to a Django form field.
    """
    css_classes = value.field.widget.attrs.get('class', '')
    if css_classes:
        if arg not in css_classes.split():
            css_classes += f' {arg}'
    else:
        css_classes = arg
    return value.as_widget(attrs={'class': css_classes})
