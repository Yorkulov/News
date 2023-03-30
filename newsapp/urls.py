from django.urls import path
from .views import newsList, newsDetail

urlpatterns = [
    path('all/', newsList, name='AllNewsList'),
    path('<int:id>/', newsDetail, name="NewsDetail"),
]
