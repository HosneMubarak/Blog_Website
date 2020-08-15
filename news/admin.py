from django.contrib import admin

from .models import NewsCategory, NewsModel, CommentModel


class CommentInline(admin.TabularInline):
    model = CommentModel


class NewsModelAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(NewsModel, NewsModelAdmin)
admin.site.register(NewsCategory)
admin.site.register(CommentModel)
