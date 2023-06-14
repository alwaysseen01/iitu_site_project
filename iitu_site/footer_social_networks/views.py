from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import FooterSocialNetwork
from .schemas import FooterSocialNetworkIn, FooterSocialNetworkOut

# Create your views here.
router = Router(tags=["Footer social networks' icons"])


@router.post("/")
async def create_social_network_item(request, data_in: FooterSocialNetworkIn):
    social_network_item = await sync_to_async(FooterSocialNetwork.objects.create)(
        icon=data_in.icon,
    )
    return {"id": social_network_item.id}


@router.put("/{social_network_item_id}/")
async def update_social_network_item(request, social_network_item_id: int, data_in: FooterSocialNetworkIn):
    try:
        social_network_item = await sync_to_async(FooterSocialNetwork.objects.get)(id=social_network_item_id)
        social_network_item.icon = data_in.icon
        await sync_to_async(social_network_item.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Social network icon not found")


@router.delete("/{social_network_item_id}/")
async def delete_social_network_item(request, social_network_item_id: int):
    try:
        social_network_item = await sync_to_async(FooterSocialNetwork.objects.get)(id=social_network_item_id)
        await sync_to_async(social_network_item.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Social network icon not found")


@router.get("/")
async def list_social_network_items(request):
    try:
        social_network_items = await sync_to_async(list)(FooterSocialNetwork.objects.all())
        return [FooterSocialNetworkOut.from_orm(item) for item in social_network_items]
    except ObjectDoesNotExist:
        raise HttpError(404, "Social network icon not found")
