from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.conf import settings
from django.views.generic import date_based, list_detail

import traceback

from blog.models import Post, Category

def post_list(request, page=0, paginate_by=20, **kwargs):
    page_size = getattr(settings,'BLOG_PAGESIZE', paginate_by)
    return list_detail.object_list(
        request,
        queryset=Post.objects.published(),
        paginate_by=page_size,
        page=page,
        **kwargs
    )


def post_archive(request, year, month=None, day=None, **kwargs):
    queryset = Post.objects.published()
    if day is not None:
        return date_based.archive_day(
            request,
            year=year,
            month=month,
            day=day,
            date_field='pub_date',
            month_format = '%m',
            queryset=queryset,
            **kwargs
        )
    elif month is not None:
        return date_based.archive_month(
            request,
            year=year,
            month=month,
            date_field='pub_date',
            month_format = '%m',
            queryset=queryset,
            **kwargs
        )
    else:
        return date_based.archive_year(
            request,
            year=year,
            date_field='pub_date',
            queryset=queryset,
            make_object_list=True,
            **kwargs
        )

def post_on_yvi(request, slug, year, month, day, **kwargs):
    post = Post.objects.get(slug=slug, pub_date__year=year, pub_date__month=int(month), pub_date__day=day)
    s = ''
    try:    
        post.post_on_yvi()
        success = True
    except:
        s = traceback.format_exc()
        success = False 
    c = RequestContext(request, {'post' : post, 'success' : success, 'msg': s})
    return render_to_response("blog/post_on_yvi_success.html", c)
    
def post_detail(request, slug, year, month, day, **kwargs):
    """
    Displays post detail. If user is superuser, view will display 
    unpublished post detail for previewing purposes.
    """
#    posts = None
#    if request.user.is_superuser:
#        posts = Post.objects.all()
#    else:
    posts = Post.objects.published()
    return date_based.object_detail(
        request,
        year=year,
        month=month,
        day=day,
        date_field='pub_date',
        month_format = '%m',
        slug=slug,
        queryset=posts,
        **kwargs
    )
    

def category_list(request, template_name = 'blog/category_list.html', **kwargs):
    """
    Category list

    Template: ``blog/category_list.html``
    Context:
        object_list
            List of categories.
    """
    return list_detail.object_list(
        request,
        queryset=Category.objects.all(),
        template_name=template_name,
        **kwargs
    )


def category_detail(request, slug, template_name = 'blog/category_detail.html', **kwargs):
    """
    Category detail

    Template: ``blog/category_detail.html``
    Context:
        object_list
            List of posts specific to the given category.
        category
            Given category.
    """
    category = get_object_or_404(Category, slug__iexact=slug)

    return list_detail.object_list(
        request,
        queryset=category.post_set.published(),
        extra_context={'category': category},
        template_name=template_name,
        **kwargs
    )
