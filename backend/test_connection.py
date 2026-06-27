from app.supabase_client import supabase

response = supabase.table("crops").select("*").execute()

print(response.data)