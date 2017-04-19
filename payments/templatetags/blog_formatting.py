from django import template

register = template.Library()


@register.filter
def format_comments(value):
    comments = ""
    for comment in value.all():
        comments += "<div><b>%s</b><br><p>%s</p></div>" % (comment.author, comment.body)
    return comments

