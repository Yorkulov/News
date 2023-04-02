from .models import News

def latestNews(request):
    latestNews = News.published.all().order_by('-publish_time')[:10]
    context = {
        'latestNews' : latestNews
    }
    return context