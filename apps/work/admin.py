from django.contrib import admin
from work.models import Project, Todo, ProjectPost

class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'is_public', 'tags', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Project, ProjectAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display  = ('title', 'pub_date')
    list_filter   = ('pub_date', 'type')
    search_fields = ('title', 'desc')
admin.site.register(Todo, TodoAdmin)

class ProjectPostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'pub_date')
    list_filter   = ('pub_date', 'category')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(ProjectPost, ProjectPostAdmin)