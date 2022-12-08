from django.urls import path

from house import views

urlpatterns = [
    path('', views.house, name="house"),
    path('details_prop/<int:id>', views.details_prop, name="details_prop"),
]
