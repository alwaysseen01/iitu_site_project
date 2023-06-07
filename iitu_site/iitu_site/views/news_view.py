from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from ..models import News
from ..schemas import NewsIn

router = Router()


@router.post("/news/")
def create_news(request, data: NewsIn):
    news = News.objects.create(**data.dict())
    return {"id": news.id}


@router.put("/news/{news_id}")
def update_news(request, news_id: int, data: NewsIn):
    try:
        news = News.objects.get(id=news_id)
        for key, value in data.dict().items():
            setattr(news, key, value)
        news.save()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "News not found")


@router.delete("/news/{news_id}")
def delete_news(request, news_id: int):
    try:
        news = News.objects.get(id=news_id)
        news.delete()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "News not found")
    