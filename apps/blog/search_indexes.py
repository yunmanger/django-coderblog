import datetime
from haystack import indexes
from haystack import site
from blog.models import Post


class PostIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_queryset(self):
        "Used when the entire index for model is updated."
        return Post.objects.published()

    def should_update(self, instance, **kwargs):
        created = kwargs.get('created',False)
        return created

site.register(Post, PostIndex)
