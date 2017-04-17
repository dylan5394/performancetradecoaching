from django import template

register = template.Library()


@register.filter
def format_comments(value):
    for comment in value.all():
        print(comment)
    return 'hello'
