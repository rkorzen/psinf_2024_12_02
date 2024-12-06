from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "is_published", "created_at"]
    list_filter = ["is_published", "created_at"]
    search_fields = ["title", "content"]
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
    actions = ["make_published"]

    def make_published(self, request, queryset):
        queryset.update(is_published=True)