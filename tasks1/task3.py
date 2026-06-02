import sqlite3

def main():
    db_name = input().strip()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    query = """
        SELECT DISTINCT year
        FROM movies
        WHERE title LIKE 'Х%'
        ORDER BY year
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row[0])
    
    conn.close()

if __name__ == "__main__":
    main()