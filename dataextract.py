import psycopg2
import pandas as pd

# --- Step 1: Database connection ---
conn = psycopg2.connect(
    host="172.20.0.4",        # or Docker container IP if remote
    port=5432,               # default PostgreSQL port
    database="chemotion",    # usually same as POSTGRES_USER
    user="postgres",        # your POSTGRES_USER
    password="postgres"      # your POSTGRES_PASSWORD
)

# --- Step 2: Query reagent data ---
query = """
SELECT * FROM Samples LIMIT 10;
"""

df = pd.read_sql(query, conn)

# --- Step 3: Export CSV ---
df.to_csv("reagents.csv", index=False)


# --- Step 5: Close connection ---
conn.close()

print("Extraction complete!")
# cur = conn.cursor()
# cur.execute("""SELECT table_schema, table_name FROM information_schema.tables
#                WHERE table_type='BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema');""")
# print(cur.fetchall())
