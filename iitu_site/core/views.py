from django.shortcuts import render
from news.models import News, MainNews
from university_advantages.models import UniversityAdvantage
from partners.models import Partners
from footer_contacts.models import ContactsElement
from footer_elements_and_categories.models import FooterElementCategory, FooterElement
from educational_programs_and_categories.models import Category, EducationalProgram


def index(request):
    news_list = News.objects.all()
    main_news = MainNews.objects.first()
    partners_list = Partners.objects.all()
    advantages_list = UniversityAdvantage.objects.all()
    contacts_list = ContactsElement.objects.all()
    footer_categories = FooterElementCategory.objects.all()
    footer_elements = FooterElement.objects.all()
    categories_list = Category.objects.all()
    programs_list = EducationalProgram.objects.all()

    context = {
        'news_list': news_list,
        'main_news': main_news,
        'partners_list': partners_list,
        'advantages_list': advantages_list,
        'contacts_list': contacts_list,
        'footer_categories': footer_categories,
        'footer_elements': footer_elements,
        'categories_list': categories_list,
        'programs_list': programs_list,
    }

    return render(request, 'index.html', context)
