import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://nhajqchezivowrlikxxx.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5oYWpxY2hleml2b3dybGlreHh4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzExMjMyMTEsImV4cCI6MjA4NjY5OTIxMX0.prWXXS1vTXMjZb0A84JAoTvWplbA_OmnkD7LdszHjW8")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
