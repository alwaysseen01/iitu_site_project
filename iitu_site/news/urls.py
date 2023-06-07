from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from views import router as news_router

api = NinjaAPI()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

api.add_router("/", news_router)
