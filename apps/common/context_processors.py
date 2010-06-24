from common.models import Link

def public_links(request):
    list = Link.objects.filter(is_public=True).order_by("-order")
    return {'public_links': list}

def markdown_config(request):
    return {'mrk_conf': "safe,extra,wikilinks(base_url=/wiki/)"}