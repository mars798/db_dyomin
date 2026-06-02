import sqlite3

def main():
    db_name = input().strip()
    artist_name = input().strip()
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    query = """
        SELECT DISTINCT Track.Name
        FROM Track
        JOIN Album ON Track.AlbumId = Album.AlbumId
        JOIN Artist ON Album.ArtistId = Artist.ArtistId
        WHERE Artist.Name = ?
        ORDER BY Track.Name
    """
    cursor.execute(query, (artist_name,))
    for row in cursor.fetchall():
        print(row[0])
    
    conn.close()

if __name__ == "__main__":
    main()