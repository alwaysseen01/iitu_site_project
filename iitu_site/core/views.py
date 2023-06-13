from django.shortcuts import render
from news.models import News, MainNews
from partners.models import Partners


def index(request):
    news_list = News.objects.all()
    main_news = MainNews.objects.first()
    partners_list = Partners.objects.all()
    context = {'news_list': news_list, 'main_news': main_news, 'partners_list': partners_list}
    return render(request, 'index.html', context)
