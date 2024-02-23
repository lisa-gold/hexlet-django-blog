from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp')
    search_fields = ['name', 'body']
    list_filter = (('timestamp', admin.DateFieldListFilter),)


# admin.site.register(Article, ArticleAdmin)
