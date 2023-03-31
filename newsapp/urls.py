from django.urls import path
from .views import newsList, newsDetail, homePageView

urlpatterns = [
    path('', homePageView, name='HomePageView'),
    path('news/', newsList, name='AllNewsList'),
    path('news/<int:id>/', newsDetail, name='NewsDetail'),
]
