from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.sitemaps import ping_google


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