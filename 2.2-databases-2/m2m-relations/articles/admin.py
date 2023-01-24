from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        k = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main')==True:
                k += 1
        if k != 1:
            raise ValidationError('Ошибка')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    inlines = [ScopeInline,]

@admin.register(Tag)
class TegAdmin(admin.ModelAdmin):
    list_display = ['name',]