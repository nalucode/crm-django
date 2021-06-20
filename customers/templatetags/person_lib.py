from django.template import Library

register = Library()


@register.filter
def cpf(value):
    '''Format the data as brazillian CPF.'''

    v = '{}.{}.{}-{}'
    v = v.format(value[:3], value[3:6], value[6:9], value[9:])

    return v


@register.filter
def br_phone(value):
    '''Format the data as brazillian phone.'''

    v = '({}) {}-{}'
    v = v.format(value[:2], value[2:7], value[7:])

    return v


@register.filter
def br_postal_code(value):
    '''Format the data as brazillian postal code.'''

    v = '{}-{}'
    v = v.format(value[:5], value[5:])

    return v
