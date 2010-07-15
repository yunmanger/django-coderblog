from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.sitemaps import ping_google
from common.utils import download_twitter_statuses, post_to_twitter
from common.django_yvi import ping_url as do_ping_url

import traceback

from django import forms

class PingForm(forms.Form):
    url         = forms.URLField()
    num         = forms.IntegerField()

@login_required
def ping_url(request, template_name="common/ping_url.html"):
    if request.user.is_superuser:
        if request.method == "POST":
            try:
                do_ping_url(request.POST['url'], int(request.POST.get('num',1)))
                msg = "Ping is OK"
            except:
                msg = traceback.format_exc()
        else:
            f = PingForm()
            c = RequestContext(request, {'form' : f})
            return render_to_response(template_name, c)
    else:
        msg = "You have no permission."
    c = RequestContext(request, {'message' : msg})
    return render_to_response("common/message.html",c)
    
@login_required
def ping(request):
    if request.user.is_superuser:
        try:
            ping_google()
            msg = "Ping is OK"
        except:
            msg = "Error pinging google."
    else:
        msg = "You have no permission."
    c = RequestContext(request, {'message' : msg})
    return render_to_response("common/message.html",c)

@login_required
def dtw(request):
    if request.user.is_superuser:
        try:
            download_twitter_statuses()
            msg = "Download twitter is OK"
        except:
            s = traceback.format_exc()
            msg = "Error twitter: %s" % s
    else:
        msg = "You have no permission."
    c = RequestContext(request, {'message' : msg})
    return render_to_response("common/message.html",c)

@login_required
def ptw(request):
    next = request.POST.get('next',None)
    next = request.GET.get('next',next)
    if request.user.is_superuser:
        try:
            post_to_twitter(request.POST.get("tweet",''))
            if next:
                return HttpResponseRedirect(next)
            msg = "Post to twitter is OK"
        except:
            s = traceback.format_exc()
            msg = "Error twitter: %s" % s
    else:
        msg = "You have no permission."
    c = RequestContext(request, {'message' : msg})
    return render_to_response("common/message.html",c)
  
    