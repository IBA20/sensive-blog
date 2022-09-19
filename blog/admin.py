from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['likes', 'tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post']
    list_display = ['author', 'published_at']
    readonly_fields = ['post']


admin.site.register(Tag)

