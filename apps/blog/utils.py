from django.conf import settings
from django.template.loader import render_to_string
from BeautifulSoup import BeautifulSoup, Comment

from common.django_yvi import post as do_post

def check(name, value):
    if (name.upper() in ['HREF', 'SRC']) and not value.upper().startswith('HTTP'):
        value = "%s%s" % (settings.DOMAIN, value)
        return name, value
    return name, value
        
def post_to_yvi(post):
    string = render_to_string("blog/post-render-yvi.html", {'object': post})
    soup = BeautifulSoup(string, selfClosingTags=['img']) 
    for tag in soup.findAll('a'):
        tag.attrs = [check(attr, val) for attr, val in tag.attrs]
    for tag in soup.findAll('img'):
        tag.attrs = [check(attr, val) for attr, val in tag.attrs]
    string = soup.renderContents()
    if post.tags == '':
        raise IOError('Tags are not specified.')
    do_post(post.title, string, post.tags, settings.YVI_LOGIN, settings.YVI_PASSWORD, settings.YVI_USER_ID)
    
def removecut(string):
    soup = BeautifulSoup(string, selfClosingTags=['img','br'])
    tag = soup.find('yvcut')
    if not tag: return string
    tag.extract()
    string = soup.renderContents()
    return string    

def postcut(string, post=None):
    soup = BeautifulSoup(string, selfClosingTags=['img','br'])
    tag = soup.find('yvcut')
    if not tag: return string
    next = tag.findAllNext()
    for t in next:
        t.extract()

    if post: url = post.get_absolute_url()
    else: url = ''
    val = tag.getText()
    newtag = "<p><a id='yvcut' href='%s'>%s</a></p>" % (url, val)
    tag.replaceWith(newtag)
    string = soup.renderContents()
    return string    
     
    
    
