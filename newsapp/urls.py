from django.urls import path
from .views import newsList, newsDetail, HomePageView, ContactPageView, notFound

urlpatterns = [
    path('', HomePageView.as_view(), name='HomePageView'),
    path('news/', newsList, name='AllNewsList'),
    path('news/<int:id>/', newsDetail, name='NewsDetail'),
    path('contact-us/', ContactPageView.as_view(), name='ContactPageView'),
    path('404/', notFound, name='NotFound'),
]
