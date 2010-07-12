from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from django.contrib.sitemaps import ping_google
from common.utils import download_twitter_statuses, post_to_twitter

import traceback


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
  
    