from django.contrib import admin

from dictionary.models import Word, Definition

# Register your models here.
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created', 'updated')

admin.site.register(Word, WordAdmin)

admin.site.register(Definition)

# class DefinitionAdmin(admin.ModelAdmin):
#     list_display = ('meaning', 'created', 'updated')

# admin.site.register(Definition, DefinitionAdmin)