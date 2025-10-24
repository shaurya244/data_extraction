from extract_text import extract_all_text
from parse_reactions import extract_reactions_from_text
from insert_to_db import insert_reaction_to_chemotion
import psycopg2
from tqdm import tqdm

conn = psycopg2.connect(
    host="db",        # or Docker container IP if remote
    port=5432,               # default PostgreSQL port
    database="chemotion",    # usually same as POSTGRES_USER
    user="postgres",        # your POSTGRES_USER
    password="postgres"      # your POSTGRES_PASSWORD
)

texts = extract_all_text("papers")

for filename, text in tqdm(texts, desc="Processing Papers"):
    reactions = extract_reactions_from_text(text)
    for r in reactions:
        try:
            insert_reaction_to_chemotion(r, conn)
        except Exception as e:
            print(f"❌ {filename}: {e}")

conn.close()
print("✅ All reactions inserted into Chemotion.")
