from .models import News, Category

def latestNews(request):
    latestNews = News.published.all().order_by('-publish_time')[:10]
    context = {
        'latestNews' : latestNews
    }
    return context

def categoryList(request):
    category = Category.objects.all().order_by('name')
    context = {
        'category' : category
    }
    return context