from asgiref.sync import sync_to_async

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import News, MainNews
from .schemas import NewsIn

router = Router(tags=["News"])
main_router = Router(tags=["Model news"])


@router.post("/")
async def create_news(request, data: NewsIn):
    news = await sync_to_async(News.objects.create)(**data.dict())
    return {"id": news.id}


@router.put("/{news_id}/")
async def update_news(request, news_id: int, data: NewsIn):
    try:
        news = await sync_to_async(News.objects.get)(id=news_id)
        for key, value in data.dict().items():
            setattr(news, key, value)
        await sync_to_async(news.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "News not found")


@router.delete("/{news_id}/")
async def delete_news(request, news_id: int):
    try:
        news = await sync_to_async(News.objects.get)(id=news_id)
        await sync_to_async(news.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "News not found")


# ------------------------------------- MAIN NEWS ---------------------------------------


@main_router.post("/")
async def create_main_news(request, data: NewsIn):
    news = await sync_to_async(MainNews.objects.create)(**data.dict())
    return {"id": news.id}


@main_router.put("/{news_id}/")
async def update_main_news(request, news_id: int, data: NewsIn):
    try:
        news = await sync_to_async(MainNews.objects.get)(id=news_id)
        for key, value in data.dict().items():
            setattr(news, key, value)
        await sync_to_async(news.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "News not found")


@main_router.delete("/{news_id}/")
async def delete_main_news(request, news_id: int):
    try:
        news = await sync_to_async(MainNews.objects.get)(id=news_id)
        await sync_to_async(news.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "News not found")
