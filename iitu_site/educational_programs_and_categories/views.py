from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from ninja import Router
from ninja.errors import HttpError

from .models import Category, EducationalProgram
from .schemas import ProgramIn, ProgramOut, CategoryIn, CategoryOut

# Create your views here.


program_router = Router(tags=["Educational Programs"])
category_router = Router(tags=["Categories of educational programs"])


@program_router.post("/")
async def create_program(request, data_in: ProgramIn):
    category = await sync_to_async(Category.objects.get)(id=data_in.category_id)
    program = await sync_to_async(EducationalProgram.objects.create)(
        category=category,
        icon=data_in.icon,
        code=data_in.code,
        title=data_in.title,
        faculties_count=data_in.faculties_count,
    )
    return {"id": program.id}


@program_router.put("/{program_id}/")
async def update_program(request, program_id: int, data_in: ProgramIn):
    try:
        program = await sync_to_async(EducationalProgram.objects.get)(id=program_id)
        program.category_id = data_in.category_id
        program.icon = data_in.icon
        program.code = data_in.code
        program.title = data_in.title
        program.faculties_count = data_in.faculties_count
        await sync_to_async(program.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Educational program not found")


@program_router.delete("/{program_id}/")
async def delete_program(request, program_id: int):
    try:
        program = await sync_to_async(EducationalProgram.objects.get)(id=program_id)
        await sync_to_async(program.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Educational program not found")


@program_router.get("/")
async def list_programs(request):
    try:
        programs = await sync_to_async(list)(EducationalProgram.objects.all())
        return [ProgramOut.from_orm(program) for program in programs]
    except ObjectDoesNotExist:
        raise HttpError(404, "Educational programs not found")


# -------------------- EDUCATIONAL PROGRAMS' CATEGORIES ------------------------------------


@category_router.post("/")
async def create_category(request, data_in: CategoryIn):
    category = await sync_to_async(Category.objects.create)(title=data_in.title)
    return {"id": category.id}


@category_router.put("/{category_id}/")
async def update_category(request, category_id: int, data_in: CategoryIn):
    try:
        category = await sync_to_async(Category.objects.get)(id=category_id)
        category.title = data_in.title
        await sync_to_async(category.save)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Category not found")


@category_router.delete("/{category_id}/")
async def delete_category(request, category_id: int):
    try:
        category = await sync_to_async(Category.objects.get)(id=category_id)
        await sync_to_async(category.delete)()
        return {"success": True}
    except ObjectDoesNotExist:
        raise HttpError(404, "Category not found")


@category_router.get("/")
async def list_categories(request):
    try:
        categories = await sync_to_async(list)(Category.objects.all())
        return [CategoryOut.from_orm(category) for category in categories]
    except ObjectDoesNotExist:
        raise HttpError(404, "Categories not found")
