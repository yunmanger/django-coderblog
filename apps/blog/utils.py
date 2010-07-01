from django.conf import settings
from django.template.loader import render_to_string
from BeautifulSoup import BeautifulSoup, Comment

from django_yvi import post as do_post

def check(name, value):
    if (name.upper() in ['HREF', 'SRC']) and not value.upper().startswith('HTTP'):
        value = "%s%s" % (settings.DOMAIN, value)
        return name, value
    return name, value
        
def post_to_yvi(post):
    string = render_to_string("blog/post-render.html", {'object': post})
    soup = BeautifulSoup(string, selfClosingTags=['img']) 
    for tag in soup.findAll('a'):
        tag.attrs = [check(attr, val) for attr, val in tag.attrs]
    for tag in soup.findAll('img'):
        tag.attrs = [check(attr, val) for attr, val in tag.attrs]
    string = soup.renderContents() 
    do_post(post.title, string ,settings.YVI_LOGIN, settings.YVI_PASSWORD, settings.YVI_USER_ID)
    