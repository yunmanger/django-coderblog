from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.conf import settings
from django.views.generic import date_based, list_detail


from work.models import Project, Todo

def project_list(request, page=0, paginate_by=20, **kwargs):
    page_size = getattr(settings,'WORK_PAGESIZE', paginate_by)
    return list_detail.object_list(
        request,
        queryset=Project.objects.published(),
        paginate_by=page_size,
        page=page,
        **kwargs
    )

def project_detail(request, slug, template_name="work/project_detail.html"):
    is_admin = request.user.is_authenticated() and request.user.is_superuser
    if is_admin:
        todos = Todo.objects.all()[:5]
    else:
        todos = Todo.objects.published()[:5]
    c = RequestContext(request, {'todo_list' : todos})
    return render_to_response(template_name, c)

def todo_list(request, slug, template_name="work/todo_list.html"):
    is_admin = request.user.is_authenticated() and request.user.is_superuser
    if is_admin:
        todos = Todo.objects.all()[:5]
    else:
        todos = Todo.objects.published()[:5]
    page_size = getattr(settings,'WORK_PAGESIZE', paginate_by)
    return list_detail.object_list(
        request,
        queryset=todos,
        paginate_by=page_size,
        page=page,
        **kwargs
    )
