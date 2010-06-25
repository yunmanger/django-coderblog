from django.contrib import admin
from blog.models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'pub_date')
    list_filter   = ('pub_date', 'category')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostAdmin)