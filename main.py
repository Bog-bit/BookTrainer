import json
import os
from datetime import datetime

FILENAME = "books.json"

def load_books():
 if not os.path.exists(FILENAME):
     return []
 try:
     with open(FILENAME, "r", encoding="utf-8") as f:
         return json.load(f)
 except json.JSONDecodeError:
     return []

def save_books(books):
 with open(FILENAME, "w", encoding="utf-8") as f:
     json.dump(books, f, ensure_ascii=False, indent=4)

def add_book(books):
 print("\nДобавление книги:")
 author = input("Введите автора книги: ").strip()
 title = input("Введите название книги: ").strip()
 
 for book in books:
     if book['author'].lower() == author.lower() and book['title'].lower() == title.lower():
         print("Ошибка: Такая книга уже есть в списке! (Дубликат)")
         return books

 while True:
     try:
         score = int(input("Введите вашу оценку (от 1 до 5): "))
         if 1 <= score <= 5:
             break
         print("Оценка должна быть числом от 1 до 5!")
     except ValueError:
         print("Введите корректное число!")

 date_str = input("Введите дату прочтения (ГГГГ-ММ-ДД): ").strip()
 if not date_str:
     date_str = datetime.now().strftime("%Y-%m-%d")

 new_book = {
     "author": author,
     "title": title,
     "score": score,
     "date": date_str
 }
 
 books.append(new_book)
 save_books(books)
 print(f"Книга «{title}» успешно добавлена!")
 return books

def list_and_stats(books):
 if not books:
     print("\nСписок книг пока пуст.")
     return

 print("\nСписок всех книг:")
 for idx, book in enumerate(books, 1):
     print(f"{idx}. {book['author']} — «{book['title']}» | Оценка: {book['score']} | Дата: {book['date']}")

 scores = [book['score'] for book in books]
 avg_score = sum(scores) / len(scores) if scores else 0
 print(f"\nСредняя оценка всех книг: {avg_score:.2f}")

 print("\nСтатистика по авторам (кол-во книг):")
 author_counts = {}
 for book in books:
     author_counts[book['author']] = author_counts.get(book['author'], 0) + 1
 
 for author, count in author_counts.items():
     print(f" - {author}: {count} кн.")

def delete_book(books):
 if not books:
     print("\nСписок книг пуст. Нечего удалять.")
     return books

 print("\nУдаление книги:")
 print("Вы можете удалить по индексу (1) или по паре автор+название (2)")
 choice = input("Выберите способ удаления (1/2): ").strip()

 if choice == "1":
     for idx, book in enumerate(books, 1):
         print(f"{idx}. {book['author']} — «{book['title']}»")
     try:
         index = int(input("Введите номер книги для удаления: ")) - 1
         if 0 <= index < len(books):
             removed = books.pop(index)
             save_books(books)
             print(f"Книга «{removed['title']}» удалена.")
         else:
             print("Неверный номер.")
     except ValueError:
         print("Ошибка ввода номера.")
         
 elif choice == "2":
     author = input("Введите автора: ").strip().lower()
     title = input("Введите название: ").strip().lower()
     
     updated_books = [b for b in books if not (b['author'].lower() == author and b['title'].lower() == title)]
     
     if len(updated_books) < len(books):
         save_books(updated_books)
         print("Книга успешно удалена.")
         return updated_books
     else:
         print("Книга с такими параметрами не найдена.")
 return books

def main():
 books = load_books()
 while True:
     print("\nМеню:")
     print("1. Добавить книгу")
     print("2. Показать все книги")
     print("3. Показать среднюю оценку")
     print("4. Статистика по авторам")
     print("5. Удалить книгу")
     print("6. Выход")
     
     choice = input("Выберите пункт меню (1-6): ").strip()
     
     if choice == "1":
         books = add_book(books)
     elif choice in ["2", "3", "4"]:
         list_and_stats(books)
     elif choice == "5":
         books = delete_book(books)
     elif choice == "6":
         print("До свидания!")
         break
     else:
         print("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
 main() 
