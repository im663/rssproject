from django import template
from django.utils.duration import _get_duration_components
from django.utils.safestring import mark_safe
from django.conf import settings
import re
from urllib.parse import urlparse

register = template.Library()

@register.simple_tag
def changeStatement(status):
    return not status

@register.filter
def date_format(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

# To read cookies within django template, from http://stackoverflow.com/questions/26301447/django-read-cookie-in-template-tag
@register.simple_tag(takes_context = True)
def cookie(context, cookie_name): # could feed in additional argument to use as default value
    request = context['request']
    result = request.COOKIES.get(cookie_name,'') # I use blank as default value
    return result

# Useful for latest-posts where we combine threads and replies
# this returns the model name
@register.filter
def to_class_name(value):
    return value.__class__.__name__

@register.filter
def shorten_url(value):
    return urlparse(value).netloc

@register.filter(name='text_effects')
def custom_formating(value):
    
    # big text, [b]text[/b]
    value = re.sub(r'\[b](.+?)\[/b]', r'<div class="big-text">\1</div>', value)

    # blue text, (((text)))
    value = re.sub(r'\(\(\((.+?)\)\)\)', r'<div class="blue-text">(((\1)))</div>', value)

    # bold text, **text**
    value = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', value)

    # button text, [button]text[/button]
    value = re.sub(r'\[button](.+?)\[/button]', r'<button class="userbutton">\1</button>', value)
    
    # glow text, %%text%%
    value = re.sub(r'\%\%(.+?)\%\%', r'<div class="glow-text">\1</div>', value)

    # green text, >text (until <br>)
    value = re.sub(r'\&gt;(.*?)($|<br>)', r'<div class="green-text">&gt;\1</div><br>', value)

    # holy text, {{text}}
    value = re.sub(r'\{\{(.+?)\}\}', r'<div class="holy-text">\1</div>', value)

    # pink text, <text (until <br> or newline)
    value = re.sub(r'\&lt;(.*?)($|<br>)', r'<div class="pink-text">&lt;\1</div><br>', value)

    # rainbow text, [r]text[/r]
    value = re.sub(r'\[r](.+?)\[/r]', r'<div class="rainbow-text">\1</div>', value)

    # red text, ==text==
    value = re.sub(r'\=\=(.+?)\=\=', r'<div class="red-text">\1</div>', value)

    # shake text, [s]text[/s]
    value = re.sub(r'\[s](.+?)\[/s]', r'<div class="shake-text">\1</div>', value)

    # spoiler text, [spoiler]text[/spoiler]
    value = re.sub(r'\[spoiler](.+?)\[/spoiler]', r'<div class="spoiler">\1</div>', value)

    # strikethrough, ~~text~~
    value = re.sub(r'\~\~(.+?)\~\~', r'<s>\1</s>', value)

    # threed text, [t]text[/t]
    value = re.sub(r'\[t](.+?)\[/t]', r'<div class="threed-text">\1</div>', value)

    # underline, __text__
    value = re.sub(r'\_\_(.+?)\_\_', r'<u>\1</u>', value)

    return(mark_safe(value))

