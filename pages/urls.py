from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('agent_grid', views.agent_grid, name='agent_grid'),
    # path('search', views.search, name='search'),
]
