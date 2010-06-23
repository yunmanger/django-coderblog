from common.models import Link

def public_links(request):
    list = Link.objects.filter(is_public=True).order_by("-order")
    return {'public_links': list}

