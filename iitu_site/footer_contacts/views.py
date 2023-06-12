from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import ContactsElement
from .schemas import ContactsElementIn, ContactsElementOut

# Create your views here.
router = Router(tags=["Footer Contacts' elements"])


@router.post("/")
async def create_contact_element(request, data_in: ContactsElementIn):
    contact_element = await sync_to_async(ContactsElement.objects.create)(
        icon=data_in.icon,
        title=data_in.title,
    )
    return {"id": contact_element.id}


@router.put("/{contact_element_id}/")
async def update_contact_element(request, contact_element_id: int, data_in: ContactsElementIn):
    try:
        contact_element = await sync_to_async(ContactsElement.objects.get)(id=contact_element_id)
        contact_element.icon = data_in.icon
        contact_element.title = data_in.title
        await sync_to_async(contact_element.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer element not found")


@router.delete("/{contact_element_id}/")
async def delete_contact_element(request, contact_element_id: int):
    try:
        contact_element = await sync_to_async(ContactsElement.objects.get)(id=contact_element_id)
        await sync_to_async(contact_element.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer element not found")


@router.get("/")
async def list_contact_elements(request):
    try:
        contact_elements = await sync_to_async(list)(ContactsElement.objects.all())
        return [ContactsElementOut.from_orm(element) for element in contact_elements]
    except ObjectDoesNotExist:
        raise HttpError(404, "Footer elements not found")
