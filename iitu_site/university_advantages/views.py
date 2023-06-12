from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from ninja import Router
from ninja.errors import HttpError

from .models import UniversityAdvantage
from .schemas import UniversityAdvantageIn

router = Router(tags=["University advantages"])


@router.post("/")
async def create_advantage(request, data: UniversityAdvantageIn):
    advantage = await sync_to_async(UniversityAdvantage.objects.create)(**data.dict())
    return {"id": advantage.id}


@router.put("/{advantage_id}/")
async def update_advantage(request, advantage_id: int, data: UniversityAdvantageIn):
    try:
        advantage = await sync_to_async(UniversityAdvantage.objects.get)(id=advantage_id)
        for key, value in data.dict().items():
            setattr(advantage, key, value)
        await sync_to_async(advantage.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "University advantage not found")


@router.delete("/{advantage_id}/")
async def delete_advantage(request, advantage_id: int):
    try:
        advantage = await sync_to_async(UniversityAdvantage.objects.get)(id=advantage_id)
        await sync_to_async(advantage.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "University advantage not found")
