from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from blog.models import Post

def post_list(request, template_name="blog/post-list.html"):
    list = Post.objects.all()
    c = RequestContext(request, {'object_list' : list})
    return render_to_response(template_name, c)
