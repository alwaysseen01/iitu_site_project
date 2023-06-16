from django.shortcuts import render

# Create your views here.
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import NavigationElement
from .schemas import NavigationElementIn, NavigationElementOut

# Create your views here.
router = Router(tags=["Header navigation elements"])


@router.post("/")
async def create_navigation_element(request, data_in: NavigationElementIn):
    navigation_element = await sync_to_async(NavigationElement.objects.create)(
        title=data_in.title,
    )
    return {"id": navigation_element.id}


@router.put("/{navigation_element_id}/")
async def update_navigation_element(request, navigation_element_id: int, data_in: NavigationElementIn):
    try:
        navigation_element = await sync_to_async(NavigationElement.objects.get)(id=navigation_element_id)
        navigation_element.title = data_in.title
        await sync_to_async(navigation_element.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header navigation element not found")


@router.delete("/{navigation_element_id}/")
async def delete_navigation_element(request, navigation_element_id: int):
    try:
        navigation_element = await sync_to_async(NavigationElement.objects.get)(id=navigation_element_id)
        await sync_to_async(navigation_element.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header navigation element not found")


@router.get("/")
async def list_navigation_elements(request):
    try:
        navigation_elements = await sync_to_async(list)(NavigationElement.objects.all())
        return [NavigationElementOut.from_orm(element) for element in navigation_elements]
    except ObjectDoesNotExist:
        raise HttpError(404, "Header navigation elements not found")
