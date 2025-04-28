from django import template

register = template.Library()

@register.filter
def formata_preco(value):
    return f"R$ {value:.2f}".replace('.', ',')
