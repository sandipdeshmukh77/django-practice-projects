from django import template
register=template.Library()

@register.filter(name='nupper')
def first_n_upper(value,n):
    result=value[0:n].upper()+value[n:]
    return result
