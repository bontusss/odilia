from django.contrib import admin

from dictionary.models import Jargon,Category, Author

# Register your models here.
# class JargonAdmin(admin.ModelAdmin):
    # list_display = ('name', 'author', 'created', 'updated')

# admin.site.register(Jargon, JargonAdmin)

admin.site.register(Jargon)
admin.site.register(Category)
admin.site.register(Author)

# class DefinitionAdmin(admin.ModelAdmin):
#     list_display = ('meaning', 'created', 'updated')

# admin.site.register(Definition, DefinitionAdmin)