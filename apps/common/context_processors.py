from common.models import Link, TwitterStatus

def public_links(request):
    list = Link.objects.filter(is_public=True).order_by("-order")
    return {'public_links': list}

def markdown_config(request):
    return {'mrk_conf': "safe,extra,wikilinks(base_url=/wiki/)"}

def twitter_statuses(request):
    return {'twitter_statuses': TwitterStatus.objects.order_by("-pub_date")[:10]}