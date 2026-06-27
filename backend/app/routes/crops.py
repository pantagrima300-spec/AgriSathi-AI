from fastapi import APIRouter, HTTPException
from app.schemas.crop_schema import Crop, CropUpdate
from app.services.crop_service import (
    get_all_crops,
    get_crop,
    create_crop,
    update_crop,
    delete_crop,
    search_crop,
)

router = APIRouter(
    prefix="/api/crops",
    tags=["Crops"],
)


@router.get("/")
def read_all_crops():
    data = get_all_crops()

    return {
        "success": True,
        "count": len(data),
        "data": data,
    }


@router.get("/{crop_id}")
def read_crop(crop_id: int):
    data = get_crop(crop_id)

    if not data:
        raise HTTPException(status_code=404, detail="Crop not found")

    return {
        "success": True,
        "data": data[0],
    }


@router.post("/", status_code=201)
def add_crop(crop: Crop):
    data = create_crop(crop.model_dump())

    return {
        "success": True,
        "message": "Crop created successfully",
        "data": data,
    }


@router.put("/{crop_id}")
def edit_crop(crop_id: int, crop: CropUpdate):
    data = update_crop(
        crop_id,
        crop.model_dump(exclude_unset=True),
    )

    if not data:
        raise HTTPException(status_code=404, detail="Crop not found")

    return {
        "success": True,
        "message": "Crop updated successfully",
        "data": data,
    }


@router.delete("/{crop_id}")
def remove_crop(crop_id: int):
    data = delete_crop(crop_id)

    if not data:
        raise HTTPException(status_code=404, detail="Crop not found")

    return {
        "success": True,
        "message": "Crop deleted successfully",
    }


@router.get("/search/")
def search(name: str):
    data = search_crop(name)

    return {
        "success": True,
        "count": len(data),
        "data": data,
    }