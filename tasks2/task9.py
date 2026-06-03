import sqlite3

def init_users_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def register_user():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    username = input("Уникальное имя пользователя: ")
    email = input("Адрес электронной почты: ")
    password = input("Пароль: ")
    password_repeat = input("Повтор пароля: ")

    if password != password_repeat:
        print("Пароли не совпадают")
        conn.close()
        return

    # проверка существования имени
    cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if cur.fetchone():
        print("Имя пользователя уже существует")
        conn.close()
        return

    # проверка существования email
    cur.execute("SELECT 1 FROM users WHERE email = ?", (email,))
    if cur.fetchone():
        print("Адрес электронной почты уже используется")
        conn.close()
        return

    # добавление нового пользователя
    cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password))
    conn.commit()
    print("Пользователь добавлен")
    conn.close()

def main():
    init_users_db()
    while True:
        register_user()
        print()  # пустая строка для разделения итераций

if __name__ == "__main__":
    main()