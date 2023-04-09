from modeltranslation.translator import register, TranslationOptions
from .models import News, Category

@register(News)
class NewsTranlationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name')

