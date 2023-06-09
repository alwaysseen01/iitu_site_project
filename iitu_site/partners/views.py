# Create your views here.
from asgiref.sync import sync_to_async

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import Partners
from .schemas import PartnerIn

router = Router(tags=["Partners"])


@router.post("/")
async def create_partner(request, data: PartnerIn):
    partner = await sync_to_async(Partners.objects.create)(**data.dict())
    return {"id": partner.id}


@router.put("/{partner_id}")
async def update_partner(request, partner_id: int, data: PartnerIn):
    try:
        partner = await sync_to_async(Partners.objects.get)(id=partner_id)
        for key, value in data.dict().items():
            setattr(partner, key, value)
        await sync_to_async(partner.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Partner not found")


@router.delete("/{partner_id}")
async def delete_partner(request, partner_id: int):
    try:
        partner = await sync_to_async(Partners.objects.get)(id=partner_id)
        await sync_to_async(partner.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Partner not found")
