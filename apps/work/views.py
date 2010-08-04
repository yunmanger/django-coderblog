from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.conf import settings
from django.views.generic import date_based, list_detail
from django.contrib.auth.decorators import login_required


from work.models import Project, Todo, ProjectPost
from work.forms import TodoForm

def project_list(request, page=0, paginate_by=20, **kwargs):
    page_size = getattr(settings,'WORK_PAGESIZE', paginate_by)
    return list_detail.object_list(
        request,
        queryset=Project.objects.published(),
        paginate_by=page_size,
        page=page,
        **kwargs
    )
    
def post_list(request, slug, page=0, paginate_by=20, **kwargs):
    page_size = getattr(settings,'BLOG_PAGESIZE', paginate_by)
    is_admin = request.user.is_authenticated() and request.user.is_superuser
    project = get_object_or_404(Project, slug__iexact=slug)
    if is_admin:
        q = project.projectpost_set.all()
    else:
        q = project.projectpost_set.published()
        
    return list_detail.object_list(
        request,
        queryset=q,
        paginate_by=page_size,
        page=page,
        extra_context= {'object' : project },
        **kwargs
    )    

def post_detail(request, slug, id, template_name="work/projectpost_detail.html"):
    project = get_object_or_404(Project, slug__iexact=slug)
    post = get_object_or_404(ProjectPost, pk=id, project=project)
    c = RequestContext(request, {'object': post})
    return render_to_response(template_name, c)

def todo_detail(request, slug, id, template_name="work/todo_detail.html"):
    project = get_object_or_404(Project, slug__iexact=slug)
    todo = get_object_or_404(Todo, pk=id, project=project)
    c = RequestContext(request, {'object': todo})
    return render_to_response(template_name, c)

def project_detail(request, slug, template_name="work/project_detail.html"):
    is_admin = request.user.is_authenticated() and request.user.is_superuser
    project = get_object_or_404(Project, slug__iexact=slug)
    if is_admin:
        todos = project.todo_set.all()[:5]
    else:
        todos = project.todo_set.published()[:5]
    if is_admin:
        posts = project.projectpost_set.all()[:5]
    else:
        posts = project.projectpost_set.published()[:5]
    c = RequestContext(request, {'object':project, 'todo_list' : todos, 'post_list': posts})
    return render_to_response(template_name, c)

def todo_list(request, slug, page=1, **kw):
    is_admin = request.user.is_authenticated() and request.user.is_superuser
    project = get_object_or_404(Project, slug__iexact=slug)
    if is_admin:
        todos = project.todo_set.all()
    else:
        todos = project.todo_set.published()
    page = request.GET.get('page',page)
    page_size = getattr(settings,'WORK_PAGESIZE', 50)
    return list_detail.object_list(
        request,
        queryset=todos,
        paginate_by=page_size,
        page=page,
        extra_context = {'object' : project },
        **kw
    )
    
@login_required
def todo_form(request, slug, id=None, template_name="work/todo_form.html"):
    is_admin = request.user.is_authenticated() and request.user.is_superuser
    if not is_admin: raise Http404
    project = get_object_or_404(Project, slug__iexact=slug)
    todo = None
    if id is not None:
        try:
            if is_admin:
                todo = project.todo_set.all().get(pk=id)
            else:
                todo = project.todo_set.published().get(pk.id)
        except Todo.DoesNotExist:
            raise Http404
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save(user=request.user, project=project)
            return HttpResponseRedirect(project.link())
    else:
        form = TodoForm(instance=todo)
    c = RequestContext(request, {'form' : form})
    return render_to_response(template_name, c)
