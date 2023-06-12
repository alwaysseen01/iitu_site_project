from django.shortcuts import render

# Create your views here.
from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import FooterElement, FooterElementCategory
from .schemas import FooterElementIn, FooterElementOut, FooterElementCategoryIn, FooterElementCategoryOut

# Create your views here.


element_router = Router(tags=["Footer elements"])
element_category_router = Router(tags=["Categories of footer elements"])


@element_router.post("/")
async def create_footer_element(request, data_in: FooterElementIn):
    category = await sync_to_async(FooterElementCategory.objects.get)(id=data_in.category_id)
    element = await sync_to_async(FooterElement.objects.create)(
        category=category,
        title=data_in.title,
    )
    return {"id": element.id}


@element_router.put("/{element_id}/")
async def update_footer_element(request, element_id: int, data_in: FooterElementIn):
    try:
        element = await sync_to_async(FooterElement.objects.get)(id=element_id)
        element.category_id = data_in.category_id
        element.title = data_in.title
        await sync_to_async(element.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer element not found")


@element_router.delete("/{element_id}/")
async def delete_footer_element(request, element_id: int):
    try:
        program = await sync_to_async(FooterElement.objects.get)(id=element_id)
        await sync_to_async(program.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer element not found")


@element_router.get("/")
async def list_footer_elements(request):
    try:
        programs = await sync_to_async(list)(FooterElement.objects.all())
        return [FooterElementOut.from_orm(program) for program in programs]
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer elements not found")


# --------------------------------- FOOTER CATEGORIES ------------------------------------


@element_category_router.post("/")
async def create_footer_category(request, data_in: FooterElementCategoryIn):
    category = await sync_to_async(FooterElementCategory.objects.create)(title=data_in.title)
    return {"id": category.id}


@element_category_router.put("/{category_id}/")
async def update_footer_category(request, category_id: int, data_in: FooterElementCategoryIn):
    try:
        category = await sync_to_async(FooterElementCategory.objects.get)(id=category_id)
        category.title = data_in.title
        await sync_to_async(category.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer category not found")


@element_category_router.delete("/{category_id}/")
async def delete_footer_category(request, category_id: int):
    try:
        category = await sync_to_async(FooterElementCategory.objects.get)(id=category_id)
        await sync_to_async(category.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer category not found")


@element_category_router.get("/")
async def list_footer_categories(request):
    try:
        categories = await sync_to_async(list)(FooterElementCategory.objects.all())
        return [FooterElementCategoryOut.from_orm(category) for category in categories]
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer categories not found")
