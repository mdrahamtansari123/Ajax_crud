from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['id','title','description']

    def __str__(self):
        return super().title