from app.supabase_client import supabase


def get_all_crops():
    response = supabase.table("crops").select("*").execute()
    return response.data


def get_crop(crop_id: int):
    response = (
        supabase
        .table("crops")
        .select("*")
        .eq("id", crop_id)
        .execute()
    )

    return response.data


def create_crop(crop_data: dict):
    response = (
        supabase
        .table("crops")
        .insert(crop_data)
        .execute()
    )

    return response.data


def update_crop(crop_id: int, crop_data: dict):
    response = (
        supabase
        .table("crops")
        .update(crop_data)
        .eq("id", crop_id)
        .execute()
    )

    return response.data


def delete_crop(crop_id: int):
    response = (
        supabase
        .table("crops")
        .delete()
        .eq("id", crop_id)
        .execute()
    )

    return response.data


def search_crop(name: str):
    response = (
        supabase
        .table("crops")
        .select("*")
        .ilike("crop", f"%{name}%")
        .execute()
    )

    return response.data