from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado','publicado','autor')
    raw_id_fields = ('autor',)
    search_fields = ('title', 'conteudo',)
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publicado'