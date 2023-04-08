from django.urls import path
from .views import newsList, newsDetail, notFound, HomePageView, ContactPageView, \
    LocalNewsView, ForeignNewsView, JamiyatNewsView, IqtisodiyotNewsView, SportNewsView, TechnologyNewsView, \
    NewsUpdateView, NewsDeleteView, NewsCreateView, admin_page_view, SearchResultList

urlpatterns = [
    path('', HomePageView.as_view(), name='HomePageView'),
    path('news/', newsList, name='AllNewsList'),
    path("news/create/", NewsCreateView.as_view(), name="NewsCreateView"),
    path('news/<slug:news>/', newsDetail, name='NewsDetail'),
    path("news/<slug>/edit/", NewsUpdateView.as_view(), name="news_update"),
    path("news/<slug>/delete/", NewsDeleteView.as_view(), name="news_delete"),
    path('404/', notFound, name='NotFound'),
    path('contact-us/', ContactPageView.as_view(), name='ContactPageView'),
    path('jamiyat-news/', JamiyatNewsView.as_view(), name='JamiyatNewsView'),
    path('local-news/', LocalNewsView.as_view(), name='LocalNewsView'),
    path('foreign-news/', ForeignNewsView.as_view(), name='ForeignNewsView'),
    path('iqtisodiyot-news/', IqtisodiyotNewsView.as_view(), name='IqtisodiyotNewsView'),
    path('sport-news/', SportNewsView.as_view(), name='SportNewsView'),
    path('technology-news/', TechnologyNewsView.as_view(), name='TechnologyNewsView'),
    path("adminpage/", admin_page_view, name='admin_page_view'),
    path('searchresult/', SearchResultList.as_view(), name="search_results"),
]
