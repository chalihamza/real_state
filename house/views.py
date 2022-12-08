from django.shortcuts import render, get_object_or_404

# Create your views here.
from house.models import House_property

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def house(request):
    all_house = House_property.objects.all()
    search_city = House_property.objects.values_list('city', flat=True).distinct()
    search_Bedrooms = House_property.objects.values_list('BedsRoom', flat=True).distinct()
    search_Garages = House_property.objects.values_list('Garages', flat=True).distinct()
    search_Bathrooms = House_property.objects.values_list('Bath', flat=True).distinct()
    search_price = House_property.objects.values_list('price', flat=True).distinct()
    search_Status = House_property.objects.values_list('Status', flat=True).distinct()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_house, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    data = {
        'all_house': users,
        'search_city': search_city,
        'search_Bedrooms': search_Bedrooms,
        'search_price': search_price,
        'search_Bathrooms': search_Bathrooms,
        'search_Garages': search_Garages,
        'search_Status': search_Status,
    }
    return render(request, 'pages/house_property.html', data)


def details_prop(request, id):
    house_property = House_property.objects.get(id=id)
    data = {
        'house_property': house_property,

    }
    return render(request, 'pages/details_prop.html', data)
