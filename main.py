import json
import os

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        print("Файл данных не найден, создана пустая коллекция.")
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

def add_book(title, author, rating):
    if not title or not author or not rating:
        print("Ошибка: все поля должны быть заполнены")
        return
    try:
        r = int(rating)
        if r < 1 or r > 5:
            print("Ошибка: оценка должна быть от 1 до 5")
            return
    except ValueError:
        print("Ошибка: оценка должна быть числом")
        return
    books = load_books()
    books.append({"title": title, "author": author, "rating": rating})
    save_books(books)
    print("Книга добавлена")

def list_books(sort_by='title'):
    books = load_books()
    if not books:
        print("Список пуст")
        return
    if sort_by == 'title':
        books.sort(key=lambda x: x['title'])
    elif sort_by == 'rating':
        books.sort(key=lambda x: x['rating'], reverse=True)
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} — {book['author']} (оценка: {book['rating']})")

def delete_book(index):
    books = load_books()
    if 0 < index <= len(books):
        books.pop(index - 1)
        print("Книга удалена.")
        save_books(books)
    else:
        print("Неверный номер")

def edit_book(index):
    books = load_books()
    if 0 < index <= len(books):
        book = books[index - 1]
        print(f"Редактирование: {book['title']} — {book['author']}")
        title = input(f"Новое название (Enter чтобы оставить '{book['title']}'): ")
        author = input(f"Новый автор (Enter чтобы оставить '{book['author']}'): ")
        rating = input(f"Новая оценка (Enter чтобы оставить '{book['rating']}'): ")
        if title: book['title'] = title
        if author: book['author'] = author
        if rating: book['rating'] = rating
        save_books(books)
        print("Книга обновлена")
    else:
        print("Неверный номер")

def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать список")
        print("3. Удалить книгу")
        print("4. Редактировать книгу")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            rating = input("Оценка (1-5): ")
            add_book(title, author, rating)
        elif choice == "2":
            list_books()
        elif choice == "3":
            list_books()
            try:
                idx = int(input("Номер для удаления: "))
                delete_book(idx)
            except ValueError:
                print("Введите число")
        elif choice == "4":
            list_books()
            try:
                idx = int(input("Номер для редактирования: "))
                edit_book(idx)
            except ValueError:
                print("Введите число")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
