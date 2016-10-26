from django.contrib import admin

from magazine.models import NewsArticle


class NewsArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = NewsArticle
