from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from newsapp.custom_permissions import UserSuperPermissions
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import News, Category, Comment
from .forms import ContactForm, CommentForm

from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin, HitCountDetailView


def newsList(request):
    # newsList = News.objects.all()
    # newsList = News.published.all()
    newsList = News.objects.filter(status=News.Status.Published)
    context = {
        "newsList": newsList
    }
    return render(request, "news/newsList.html", context)


def newsDetail(request, news):
    newsDetail = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {}
    # hitcount logikasi
    hit_count = get_hitcount_model().objects.get_for_object(newsDetail)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk' : hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    comments = newsDetail.comments.filter(active=True)
    new_comment = None

    comment_count = comments.count() # izohlar soni
    # newsDetail.view_count = newsDetail.view_count + 1
    # newsDetail.save()   # comment .models qismida
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #yangi comment obyektini yaratamiz lekin DB ga saqlamaymiz
            new_comment = comment_form.save(commit=False)
            new_comment.news = newsDetail
            #izoh egasin iso'rov yuborayotgan userga bog'lash
            new_comment.user = request.user
            #malumotlar bazasiga saqlaymiz
            new_comment.save()
            comment_form = CommentForm() # izoh qoldirilgandan so'ng inputdagi malumotni tozalash

    else:
        comment_form = CommentForm()
    
    context = {
        'newsDetail': newsDetail,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        "comment_count": comment_count,
    }
    return render(request, 'news/newsDetail.html', context)


# def homePageView(request):
#     newsList = News.objects.all().order_by('-publish_time')[:10]
#     localNewsOne = News.objects.all().filter(category__name = "O'zbekiston").order_by('-publish_time')[:1]
#     localNewsList = News.objects.all().filter(category__name = "O'zbekiston").order_by('-publish_time')[1:6]
#     jahonNewsOne = News.objects.all().filter(category__name = "Jahon").order_by('-publish_time')[:1]
#     jahonNewsList = News.objects.all().filter(category__name = "Jahon").order_by('-publish_time')[1:6]
#     technologyNewsOne = News.objects.all().filter(category__name = "Fan-Texnika").order_by('-publish_time')[:1]
#     technologyNewsList = News.objects.all().filter(category__name = "Fan-Texnika").order_by('-publish_time')[1:6]
#     sportNewsOne = News.objects.all().filter(category__name = "Sport").order_by('-publish_time')[:1]
#     sportNewsList = News.objects.all().filter(category__name = "Sport").order_by('-publish_time')[1:6]
#     category = Category.objects.all()
#     context = {
#         'newsList' : newsList,
#         'category' : category,
#         'localNewsOne' : localNewsOne,
#         'localNewsList' : localNewsList,
#         'jahonNewsOne' : jahonNewsOne,
#         'jahonNewsList' : jahonNewsList,
#         'technologyNewsOne' : technologyNewsOne,
#         'technologyNewsList' : technologyNewsList,
#         'sportNewsOne' : sportNewsOne,
#         'sportNewsList' : sportNewsList,
#     }
#     return render(request, "news/index.html", context)


class HomePageView(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['newsList'] = News.objects.all().order_by('-publish_time')[:15]
        context['localNewsOne'] = News.objects.all().filter(
            category__name="O'zbekiston").order_by('-publish_time')[:1]
        context['localNewsList'] = News.objects.all().filter(
            category__name="O'zbekiston").order_by('-publish_time')[1:6]
        # context['jahonNewsOne'] = News.objects.all().filter(
        #     category__name="Jahon").order_by('-publish_time')[:1]
        context['jahonNewsList'] = News.objects.all().filter(
            category__name="Jahon").order_by('-publish_time')[:6]
        # context['technologyNewsOne'] = News.objects.all().filter(
        #     category__name="Fan-Texnika").order_by('-publish_time')[:1]
        context['technologyNewsList'] = News.objects.all().filter(
            category__name="Fan-Texnika").order_by('-publish_time')[:6]
        # context['sportNewsOne'] = News.objects.all().filter(
        #     category__name="Sport").order_by('-publish_time')[:1]
        context['sportNewsList'] = News.objects.all().filter(
            category__name="Sport").order_by('-publish_time')[:6]

        return context

# class HomePageView(ListView):
#     template_name = "news/index.html"
#     newsList = News.objects.all().order_by('-publish_time')[:10]
#     context = {
#         'newsList' : newsList
#     }

#     def get_queryset(self, request):
#         return render(request, context)


def notFound(request):
    context = {

    }
    return render(request, "news/404.html", context)


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method  == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Malumotlar muvaffaqqiyatli jo'natildi! </h2>")
#     context = {
#         'form' : form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h1> Malumotlaringiz muvaffiqiyatli uzatildi </h1>")
        context = {
            "form": form
        }
        return render(request, 'news/contact.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = "news/localNews.html"
    context_object_name = "localNews"

    def get_queryset(self):
        localNews = News.published.all().filter(category__name = 'O\'zbekiston').order_by('-publish_time')
        return localNews
    

class ForeignNewsView(ListView):
    model = News
    template_name = "news/foreignNews.html"
    context_object_name = "foreignNews"

    def get_queryset(self):
        foreignNews = News.published.all().filter(category__name = 'Jahon').order_by('-publish_time')
        return foreignNews
    

class JamiyatNewsView(ListView):
    model = News
    template_name = "news/jamiyatNews.html"
    context_object_name = "jamiyatNews"

    def get_queryset(self):
        jamiyatNews = News.published.all().filter(category__name = 'Jamiyat').order_by('-publish_time')
        return jamiyatNews
    

class IqtisodiyotNewsView(ListView):
    model = News
    template_name = "news/iqtisodiyotNews.html"
    context_object_name = "iqtisodiyotNews"

    def get_queryset(self):
        iqtisodiyotNews = News.published.all().filter(category__name = 'Iqtisodiyot').order_by('-publish_time')
        return iqtisodiyotNews
    

class TechnologyNewsView(ListView):
    model = News
    template_name = "news/technologyNews.html"
    context_object_name = "technologyNews"

    def get_queryset(self):
        technologyNews = News.published.all().filter(category__name = 'Fan-Texnika').order_by('-publish_time')
        return technologyNews
    

class SportNewsView(ListView):
    model = News
    template_name = "news/sportNews.html"
    context_object_name = "sportNews"

    def get_queryset(self):
        sportNews = News.published.all().filter(category__name = 'Sport').order_by('-publish_time')
        return sportNews
    

class NewsUpdateView(UserSuperPermissions, UpdateView):
    model = News
    fields = ['title', 'body', 'image', 'category', 'status']
    template_name = "crud/newsEdit.html"


class NewsDeleteView(UserSuperPermissions, DeleteView):
    model = News
    template_name = "crud/newsDelete.html"
    success_url = reverse_lazy('HomePageView')


class NewsCreateView(UserSuperPermissions, CreateView):
    model = News
    template_name = "crud/newsCreate.html"
    fields = ('title', 'title_uz', 'title_en', 'title_ru', 'slug', 'image', 'body', 'body_uz', 'body_en', 'body_ru', 'category', 'status')

@login_required
@user_passes_test(lambda u:u.is_superuser)
def admin_page_view(request):
    admin_users = User.objects.filter(is_superuser=True)
    context = {
        "admin_users": admin_users
    }
    return render(request, "pages/admin_page.html", context)


class SearchResultList(ListView):
    model = News
    template_name = "news/search.html"
    context_object_name = 'all_news'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query) # title hamda bodydan qidirish
        )