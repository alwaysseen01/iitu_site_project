"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the 'include()' function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from news.views import router as news_router
from partners.views import router as partners_router
from educational_programs_and_categories.views import program_router, category_router
from university_advantages.views import router as university_advantages_router
from footer_elements_and_categories.views import element_router, element_category_router
from footer_contacts.views import router as footer_contacts_router

from .views import index


api = NinjaAPI()

api.add_router("news", news_router)
api.add_router("partners", partners_router)
api.add_router("educational_programs", program_router)
api.add_router("categories_of_educational_programs", category_router)
api.add_router("university_advantages", university_advantages_router)
api.add_router("footer_elements", element_router)  # Footer elements
api.add_router("categories_of_footer_elements", element_category_router)  # Category of Footer elements
api.add_router("categories_of_contacts_elements", footer_contacts_router)  # Footer contacts' elements

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("home/", index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
