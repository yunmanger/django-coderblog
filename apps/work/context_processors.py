from work.models import ProjectPost, Project

def recent_projectposts(request):
    list = ProjectPost.objects.published().order_by("-pub_date")[:10]
    return {'recent_projectposts': list}

def project_list(request):
    list = Project.objects.published().order_by("-pub_date")
    return {'project_list': list}
