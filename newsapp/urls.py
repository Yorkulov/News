from django.urls import path
from .views import newsList, newsDetail, notFound, HomePageView, ContactPageView, \
    LocalNewsView, ForeignNewsView, JamiyatNewsView, IqtisodiyotNewsView, SportNewsView, TechnologyNewsView 

urlpatterns = [
    path('', HomePageView.as_view(), name='HomePageView'),
    path('news/', newsList, name='AllNewsList'),
    path('news/<slug:news>/', newsDetail, name='NewsDetail'),
    path('contact-us/', ContactPageView.as_view(), name='ContactPageView'),
    path('404/', notFound, name='NotFound'),
    path('jamiyat-news/', JamiyatNewsView.as_view(), name='JamiyatNewsView'),
    path('local-news/', LocalNewsView.as_view(), name='LocalNewsView'),
    path('foreign-news/', ForeignNewsView.as_view(), name='ForeignNewsView'),
    path('iqtisodiyot-news/', IqtisodiyotNewsView.as_view(), name='IqtisodiyotNewsView'),
    path('sport-news/', SportNewsView.as_view(), name='SportNewsView'),
    path('technology-news/', TechnologyNewsView.as_view(), name='TechnologyNewsView'),
]
