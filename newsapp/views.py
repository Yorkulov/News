from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import News, Category, Contact

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

def contactPageView(request):
    form = Contact(request.POST or None)
    if request.method  == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2>Malumotlar muvaffaqqiyatli jo'natildi!</h2>")
    context = {
        'form' : form
    }
    return render(request, 'news/contact.html', context)

def notFound(request):
    context = {

    }
    return render(request, "news/404.html", context)

