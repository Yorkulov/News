from django.urls import path
from .views import newsList, newsDetail, homePageView, contactPageView, notFound

urlpatterns = [
    path('', homePageView, name='HomePageView'),
    path('news/', newsList, name='AllNewsList'),
    path('news/<int:id>/', newsDetail, name='NewsDetail'),
    path('contact-us/', contactPageView, name='ContactPageView'),
    path('404/', notFound, name='NotFound'),
]
