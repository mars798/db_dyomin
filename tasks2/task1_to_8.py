import sqlite3

# Задача №1: удалить все комедии
def task1(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("DELETE FROM films WHERE genre = 'комедия'")
    conn.commit()
    conn.close()

# Задача №2: пустую длительность (пустая строка) заменить на 42
def task2(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("UPDATE films SET duration = 42 WHERE duration = ''")
    conn.commit()
    conn.close()

# Задача №3: удвоить длительность фантастических фильмов
def task3(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("UPDATE films SET duration = duration * 2 WHERE genre = 'фантастика'")
    conn.commit()
    conn.close()

# Задача №4: удалить фильмы, название на "Я" и заканчивается на "а"
def task4(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("DELETE FROM films WHERE title LIKE 'Я%а'")
    conn.commit()
    conn.close()

# Задача №5: удалить боевики с длительностью >= 90 минут
def task5(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("DELETE FROM films WHERE genre = 'боевик' AND duration >= 90")
    conn.commit()
    conn.close()

# Задача №6: мюзиклы длиннее 100 минут сделать равными 100
def task6(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("UPDATE films SET duration = 100 WHERE genre = 'мюзикл' AND duration > 100")
    conn.commit()
    conn.close()

# Задача №7: фильмы 1973 года уменьшить длительность втрое
def task7(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("UPDATE films SET duration = duration / 3 WHERE year = 1973")
    conn.commit()
    conn.close()

# Задача №8: удалить фантастику до 2000 года с длительностью > 90 минут
def task8(name: str) -> None:
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("DELETE FROM films WHERE genre = 'фантастика' AND year < 2000 AND duration > 90")
    conn.commit()
    conn.close()

