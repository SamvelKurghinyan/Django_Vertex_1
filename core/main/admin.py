from django.contrib import admin
from .models import HomeBG, Post
from modeltranslation.admin import TranslationAdmin

class PostAdmin(TranslationAdmin):
    pass

admin.site.register(HomeBG)
admin.site.register(Post)
