from django.shortcuts import render

# Create your views here.
from house.models import House_property
from news.models import Blognews
from pages.models import Agent, Testimonial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    agents = Agent.objects.all()
    la_property_house = House_property.objects.order_by('-date')
    blognews = Blognews.objects.order_by('-date')
    testimonial = Testimonial.objects.order_by('-date')
    search_city = House_property.objects.values_list('city', flat=True).distinct()
    search_Bedrooms = House_property.objects.values_list('BedsRoom', flat=True).distinct()
    search_Garages = House_property.objects.values_list('Garages', flat=True).distinct()
    search_Bathrooms = House_property.objects.values_list('Bath', flat=True).distinct()
    search_price = House_property.objects.values_list('price', flat=True).distinct()
    search_Status = House_property.objects.values_list('Status', flat=True).distinct()
    page = request.GET.get('page', 1)
    paginator = Paginator(agents, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    data = {
        'agents': users,
        'la_property_house': la_property_house,
        'blognews': blognews,
        'testimonial': testimonial,
        'search_city': search_city,
        'search_Bedrooms': search_Bedrooms,
        'search_price': search_price,
        'search_Bathrooms': search_Bathrooms,
        'search_Garages': search_Garages,
        'search_Status': search_Status,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def agent_grid(request):
    all_agent = Agent.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_agent, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'all_agent': users,
    }
    return render(request, 'pages/agent_grid.html', data)


def contact(request):
    return render(request, 'pages/contact.html')
# def search(request):
#     prop = House_property.objects.order_by('-date')
#     data = {
#         'prop': prop,
#     }
#     return render(request, 'templates/search.html', data)
