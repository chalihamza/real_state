from django.shortcuts import render

# Create your views here.
from news.models import Blognews
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def news(request):
    all_blog = Blognews.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(all_blog, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    data = {
        'all_blog': users,
    }
    return render(request, 'pages/news.html', data)


def BlogSingleDetail(request, id):
    all_news = Blognews.objects.get(id=id)
    print(id)
    datt = {
        'all_news': all_news,
    }
    return render(request, 'pages/BlogSingleDetail.html', datt)
