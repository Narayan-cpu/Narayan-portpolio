from supabase import create_client, Client

SUPABASE_URL = 'https://xjwcweimbeahmsnzecpk.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhqd2N3ZWltYmVhaG1zbnplY3BrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU3ODQ2MTIsImV4cCI6MjA0MTM2MDYxMn0.RI0UG6GA2eQ2mzsfTfy2dTT_SGVj15JIZiMSR4zlgBc'

def supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
