import re
from django import template
from django.db import models
from django.utils import text

from BeautifulSoup import BeautifulSoup, Comment
from blog.utils import postcut, removecut

Post = models.get_model('blog','post')
#from blog.models import Post

register = template.Library()


class PostArchive(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        dates = Post.objects.published().dates('pub_date', 'month', order='DESC')
        if dates:
            context[self.var_name] = dates
        return ''


@register.tag
def get_post_archive(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
    var_name = m.groups()[0]
    return PostArchive(var_name)



@register.filter
def truncatehtml(string, length):
    return text.truncate_html_words(string, length)
truncatehtml.is_safe = True

@register.filter
def yvcut(string, o):
    n = len(string)
    s = postcut(string, o)
    if len(s) == len(string):
        return text.truncate_html_words(string, 256)
    else:
        return s
yvcut.is_safe = True

@register.filter
def rmcut(string):
    return removecut(string)
rmcut.is_safe = True