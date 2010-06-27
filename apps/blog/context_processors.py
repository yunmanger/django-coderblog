from blog.models import Post, Category

def recent_posts(request):
    list = Post.objects.published().order_by("-pub_date")[:10]
    return {'recent_posts': list}

def category_list(request):
    list = Category.objects.all().order_by("title")[:10]
    return {'category_list': list}
