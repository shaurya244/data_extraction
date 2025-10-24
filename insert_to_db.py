import psycopg2

def insert_reaction_to_chemotion(reaction, conn):
    cur = conn.cursor()
    r = reaction["reaction"]

    cur.execute("""
        INSERT INTO reactions (name, description, temperature, yield,user_id,collection_id)
        VALUES (%s, %s, %s, %s,%s,%s)
        RETURNING id;
    """, (
        f"Auto-import: {', '.join(r.get('reactants', []))} → {', '.join(r.get('products', []))}",
        "Imported automatically from literature",
        r.get("temperature"),
        r.get("yield"),
        2,
        1
    ))
    reaction_id = cur.fetchone()[0]

    for reagent in r.get("reactants", []):
        cur.execute("INSERT INTO reagents (name) VALUES (%s) RETURNING id;", (reagent,))
        reagent_id = cur.fetchone()[0]
        cur.execute("INSERT INTO reaction_reagents (reaction_id, reagent_id) VALUES (%s, %s);",
                    (reaction_id, reagent_id))

    for product in r.get("products", []):
        cur.execute("INSERT INTO samples (name) VALUES (%s) RETURNING id;", (product,))
        sample_id = cur.fetchone()[0]
        cur.execute("INSERT INTO reaction_products (reaction_id, sample_id) VALUES (%s, %s);",
                    (reaction_id, sample_id))

    conn.commit()
    cur.close()
