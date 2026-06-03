import sqlite3

def login_user():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    username = input("Имя пользователя: ")
    password = input("Пароль: ")

    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if row is None:
        print("Имя пользователя не найдено")
    elif row[0] == password:
        print("Авторизация успешна")
    else:
        print("Неправильный пароль")
    conn.close()

def main():
    # предполагается, что users.db уже создана системой регистрации
    while True:
        login_user()
        print()

if __name__ == "__main__":
    main()