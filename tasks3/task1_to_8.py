import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Определяем базовый класс для моделей
Base = declarative_base()

# Задача №1: Модель Author
class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    avatar_url = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', country='{self.country}')"

# Задача №5: Модель Book
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    author_id = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', year={self.year}, price={self.price})"

# Создаём engine и сессию
DB_NAME = "library.db"
engine = create_engine(f'sqlite:///{DB_NAME}', echo=False)
Base.metadata.create_all(engine)  # создаёт таблицы, если их нет
Session = sessionmaker(bind=engine)
session = Session()

# Задача №2: Добавление трёх авторов
def add_authors():
    authors_data = [
        Author(name="Лев Толстой", country="Россия", avatar_url="https://example.com/tolstoy.jpg"),
        Author(name="Джордж Оруэлл", country="Великобритания", avatar_url="https://example.com/owell.jpg"),
        Author(name="Марк Твен", country="США", avatar_url="https://example.com/twain.jpg"),
    ]
    for author in authors_data:
        # Проверяем, нет ли уже такого автора (по уникальному имени, например)
        existing = session.query(Author).filter_by(name=author.name).first()
        if not existing:
            session.add(author)
    session.commit()
    print("Авторы успешно добавлены (или уже существовали).")

# Задача №3: Функция print_authors, выводящая всех авторов
def print_authors():
    authors = session.query(Author).all()
    for author in authors:
        print(f"Имя: {author.name}, Страна: {author.country}")

# Задача №4: Функция для вывода авторов из России
def print_authors_russia():
    authors = session.query(Author).filter(Author.country == "Россия").all()
    for author in authors:
        print(f"Имя: {author.name}, Страна: {author.country}")

# Задача №6: Добавление трёх книг
def add_books():
    books_data = [
        Book(title="Война и мир", pages=1225, year=1869, rating=4.8, price=350.50, author_id=1),
        Book(title="Преступление и наказание", pages=500, year=1866, rating=4.7, price=270.00, author_id=1),
        Book(title="1984", pages=328, year=1949, rating=4.9, price=450.00, author_id=2),
    ]
    for book in books_data:
        existing = session.query(Book).filter_by(title=book.title, author_id=book.author_id).first()
        if not existing:
            session.add(book)
    session.commit()
    print("Книги успешно добавлены (или уже существовали).")

# Задача №7: Функция print_books, выводящая все книги
def print_books():
    books = session.query(Book).all()
    for book in books:
        print(f'"{book.title}" [{book.year}] {book.pages} стр. (В среднем {book.price} руб за шт.)')

# Задача №8: Функция, выводящая книги после 1860 года и не дороже 300 рублей
def print_books_cheap_after_1860():
    books = session.query(Book).filter(Book.year > 1860, Book.price <= 300).all()
    for book in books:
        print(f'"{book.title}" [{book.year}] {book.pages} стр. (В среднем {book.price} руб за шт.)')

# Демонстрация работы всех функций
if __name__ == "__main__":
    # Создаём таблицы (если не созданы)
    Base.metadata.create_all(engine)
    
    # Добавляем авторов и книги
    add_authors()
    add_books()
    
    print("\n--- Задача №3: Все авторы ---")
    print_authors()
    
    print("\n--- Задача №4: Авторы из России ---")
    print_authors_russia()
    
    print("\n--- Задача №7: Все книги ---")
    print_books()
    
    print("\n--- Задача №8: Книги после 1860 года и не дороже 300 руб ---")
    print_books_cheap_after_1860()