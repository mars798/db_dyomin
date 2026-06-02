import sqlite3

def main():
    db_name = input().strip()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    query = """
        SELECT movies.title
        FROM movies
        JOIN genres ON movies.genre_id = genres.id
        WHERE genres.name IN ('музыка', 'анимация')
          AND movies.year >= 1997
        ORDER BY movies.title
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row[0])
    
    conn.close()

if __name__ == "__main__":
    main()