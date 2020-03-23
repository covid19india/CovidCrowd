from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def links(value, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    lines = value.split("\n")
    for i, line in enumerate(lines):
        line = esc(line)
        if line.startswith("http"):
            lines[i] = f'<a href="{line}" target="_blank">{line}</a>'
    return mark_safe("\n".join(lines))


@register.inclusion_tag("patients/components/small_card.html")
def small_card(title, text, icon):
    return {"title": title, "content": text, "icon": icon}


@register.filter(name='splitlines')
def splitlines(value):
    """Returns the value turned into a list."""
    return value.split("\n")