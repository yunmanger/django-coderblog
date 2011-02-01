#coding: utf-8
import urllib2, cookielib
import ClientCookie
from ClientForm import *

def post(title, post, YVI_LOGIN, YVI_PASSWORD, YVI_USER_ID=None):
    request = ClientCookie.Request("http://yvision.kz/auth/")
    response = ClientCookie.urlopen(request)

    forms = ParseResponse(response, backwards_compat=False)
    form = forms[1]

    form.action = 'http://yvision.kz/ajax/auth/login.php'
    form['login'] = YVI_LOGIN
    form['password'] = YVI_PASSWORD
    request = form.click()
    response = ClientCookie.urlopen(request)

    request = ClientCookie.Request('http://%s.yvision.kz/manage/article/add' % YVI_LOGIN)

    #request = ClientCookie.Request('http://%s.yvision.kz/manage/article/edit/%s' % (YVI_LOGIN,POST_ID))

    response = ClientCookie.urlopen(request)
    forms = ParseResponse(response, backwards_compat=False)
    form = forms[2]

    form.action = 'http://%s.yvision.kz/ajax/post/article.php?publicate=1' % YVI_LOGIN
    form['blog_title'] = title
    form['blog_post'] = post
    form['blog_tags'] = "notag"
    if YVI_USER_ID is not None:
        form.new_control('hidden','user-id',{'id':'user-id','value':YVI_USER_ID})
    form.new_control('hidden','save',{'value':'asd'})
    form.new_control('hidden','saveexit',{'value':'asdf'})

    request = form.click()
    response = ClientCookie.urlopen(request)

