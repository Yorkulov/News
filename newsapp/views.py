from django.shortcuts import render, get_object_or_404
from .models import News, Category

def newsList(request):
    # newsList = News.objects.all()
    # newsList = News.published.all()
    newsList = News.objects.filter(status=News.Status.Published)
    context = {
        "newsList": newsList
    }
    return  render(request, "news/newsList.html", context)


def newsDetail(request, id):
    newsDetail = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'newsDetail': newsDetail
    }
    return render(request, 'news/newsDetail.html', context)

def homePageView(request):
    news = News.objects.all()
    category = Category.objects.all()
    context = {
        'news' : news,
        'category' : category
    }
    return render(request, "news/index.html", context)

