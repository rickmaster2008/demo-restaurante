from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,})

@register.filter(name='addid')
def addId(value, arg):
    return value.as_widget(attrs={'id': arg})

@register.filter(name='addplaceholder')
def addPlaceholder(value, arg):
    return value.as_widget(attrs={'placeholder': arg})