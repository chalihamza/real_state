from django.urls import path

from news import views

urlpatterns = [
    path('', views.news, name="news"),
    path('BlogSingleDetail/<int:id>', views.BlogSingleDetail, name="BlogSingleDetail"),
]
