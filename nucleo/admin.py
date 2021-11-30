from django.contrib import admin

# Esta clase nos permite filtrar contenido en la admin

from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_filter = ('tags', 'created_on', 'updated_on')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)} # Esto crea el enlace que luego se muestra en el navegador
    autocomplete_fields = ('tags',)

admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)
