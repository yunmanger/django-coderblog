from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.conf import settings
from django.views.generic import date_based, list_detail


from work.models import Project

def project_list(request, page=0, paginate_by=20, **kwargs):
    page_size = getattr(settings,'WORK_PAGESIZE', paginate_by)
    return list_detail.object_list(
        request,
        queryset=Project.objects.published(),
        paginate_by=page_size,
        page=page,
        **kwargs
    )
