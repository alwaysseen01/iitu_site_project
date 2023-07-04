from django.shortcuts import render

# Create your views here.
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import NavigationElement, DropdownNavigationElement1, DropdownNavigationElement2, \
    DropdownNavigationElement3
from .schemas import NavigationElementIn, NavigationElementOut, DropdownNavigationElement1_In, \
    DropdownNavigationElement1_Out, DropdownNavigationElement2_Out, DropdownNavigationElement2_In, \
    DropdownNavigationElement3_Out, DropdownNavigationElement3_In

# Create your views here.
router = Router(tags=["Header navigation elements"])


@router.post("/")
async def create_navigation_element(request, data_in: NavigationElementIn):
    navigation_element = await sync_to_async(NavigationElement.objects.create)(
        title=data_in.title,
        is_dropdown=data_in.is_dropdown,
    )
    return {"id": navigation_element.id}


@router.put("/{navigation_element_id}/")
async def update_navigation_element(request, navigation_element_id: int, data_in: NavigationElementIn):
    try:
        navigation_element = await sync_to_async(NavigationElement.objects.get)(id=navigation_element_id)
        navigation_element.title = data_in.title
        navigation_element.is_dropdown = data_in.is_dropdown
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


@router.post("/")
async def create_dropdown_1_element(request, data_in: DropdownNavigationElement1_In):
    dropdown_navigation_element = await sync_to_async(DropdownNavigationElement1.objects.create)(
        title=data_in.title,
        parent_navigation_element=data_in.parent_navigation_element,
        is_dropdown=data_in.is_dropdown,
    )
    return {"id": dropdown_navigation_element.id}


@router.put("/{dropdown_1_element_id}/")
async def update_dropdown_1_element(request, dropdown_1_element_id: int, data_in: DropdownNavigationElement1_In):
    try:
        dropdown_navigation_element = await sync_to_async(DropdownNavigationElement1.objects.get)(id=dropdown_1_element_id)
        dropdown_navigation_element.title = data_in.title
        dropdown_navigation_element.parent_navigation_element = data_in.parent_navigation_element
        dropdown_navigation_element.is_dropdown = data_in.is_dropdown
        await sync_to_async(dropdown_navigation_element.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation element not found")


@router.delete("/{dropdown_1_element_id}/")
async def delete_dropdown_1_element(request, dropdown_1_element_id: int):
    try:
        dropdown_navigation_element = await sync_to_async(DropdownNavigationElement1.objects.get)(id=dropdown_1_element_id)
        await sync_to_async(dropdown_navigation_element.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation element not found")


@router.get("/")
async def list_dropdown_1_elements(request):
    try:
        dropdown_navigation_elements = await sync_to_async(list)(DropdownNavigationElement1.objects.all())
        return [DropdownNavigationElement1_Out.from_orm(element) for element in dropdown_navigation_elements]
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation elements not found")

@router.post("/")
async def create_dropdown_2_element(request, data_in: DropdownNavigationElement2_In):
    dropdown_navigation_element = await sync_to_async(DropdownNavigationElement2.objects.create)(
        title=data_in.title,
        parent_navigation_element=data_in.parent_navigation_element,
        is_dropdown=data_in.is_dropdown,
    )
    return {"id": dropdown_navigation_element.id}


@router.put("/{dropdown_2_element_id}/")
async def update_dropdown_2_element(request, dropdown_2_element_id: int, data_in: DropdownNavigationElement2_In):
    try:
        dropdown_navigation_element = await sync_to_async(DropdownNavigationElement2.objects.get)(id=dropdown_2_element_id)
        dropdown_navigation_element.title = data_in.title
        dropdown_navigation_element.parent_navigation_element = data_in.parent_navigation_element
        dropdown_navigation_element.is_dropdown = data_in.is_dropdown
        await sync_to_async(dropdown_navigation_element.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation element not found")


@router.delete("/{dropdown_2_element_id}/")
async def delete_dropdown_2_element(request, dropdown_2_element_id: int):
    try:
        dropdown_navigation_element = await sync_to_async(DropdownNavigationElement2.objects.get)(id=dropdown_2_element_id)
        await sync_to_async(dropdown_navigation_element.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation element not found")


@router.get("/")
async def list_dropdown_2_elements(request):
    try:
        dropdown_navigation_elements = await sync_to_async(list)(DropdownNavigationElement2.objects.all())
        return [DropdownNavigationElement2_Out.from_orm(element) for element in dropdown_navigation_elements]
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation elements not found")


@router.post("/")
async def create_dropdown_3_element(request, data_in: DropdownNavigationElement3_In):
    dropdown_navigation_element = await sync_to_async(DropdownNavigationElement3.objects.create)(
        title=data_in.title,
        parent_navigation_element=data_in.parent_navigation_element,
    )
    return {"id": dropdown_navigation_element.id}


@router.put("/{dropdown_3_element_id}/")
async def update_dropdown_3_element(request, dropdown_3_element_id: int, data_in: DropdownNavigationElement3_In):
    try:
        dropdown_navigation_element = await sync_to_async(DropdownNavigationElement3.objects.get)(id=dropdown_3_element_id)
        dropdown_navigation_element.title = data_in.title
        dropdown_navigation_element.parent_navigation_element = data_in.parent_navigation_element
        await sync_to_async(dropdown_navigation_element.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation element not found")


@router.delete("/{dropdown_3_element_id}/")
async def delete_dropdown_3_element(request, dropdown_3_element_id: int):
    try:
        dropdown_navigation_element = await sync_to_async(DropdownNavigationElement3.objects.get)(id=dropdown_3_element_id)
        await sync_to_async(dropdown_navigation_element.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation element not found")


@router.get("/")
async def list_dropdown_3_elements(request):
    try:
        dropdown_navigation_elements = await sync_to_async(list)(DropdownNavigationElement3.objects.all())
        return [DropdownNavigationElement3_Out.from_orm(element) for element in dropdown_navigation_elements]
    except ObjectDoesNotExist:
        raise HttpError(404, "Header dropdown navigation elements not found")
