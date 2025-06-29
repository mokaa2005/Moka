from django.contrib import admin

from .models import post,comment


class CommentAdminInline(admin.TabularInline):
    model = comment
    fields=['text']
    extra=0


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','is_enable', 'publish_date', 'created_time')
    inlines = [CommentAdminInline,]

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('post','text','created_time')


admin.site.register(post, PostAdmin)
# admin.site.register(comment, CommentAdmin)

