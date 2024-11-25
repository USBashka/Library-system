import unittest
from unittest.mock import patch
from main import Book, get_plural_books, print_table_of_books, books, last_id



class TestBook(unittest.TestCase):
    def setUp(self):
        """Подготовка окружения перед каждым тестом"""
        books.clear()  # Очистка списка книг
        global last_id
        last_id = 0  # Сброс ID

    def test_create_book(self):
        """Тест создания книги"""
        book = Book(1, "Test Book", "Test Author", 2023)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "в наличии")
        self.assertIn(book, books)

    def test_book_to_dict(self):
        """Тест преобразования книги в словарь"""
        book = Book(1, "Test Book", "Test Author", 2023)
        expected_dict = {
            "id": 1,
            "title": "Test Book",
            "author": "Test Author",
            "year": 2023,
            "status": "в наличии"
        }
        self.assertEqual(book.to_dict(), expected_dict)

    def test_book_from_dict(self):
        """Тест создания книги из словаря"""
        data = {
            "id": 1,
            "title": "Test Book",
            "author": "Test Author",
            "year": 2023,
            "status": "в наличии"
        }
        book = Book.from_dict(data)
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "в наличии")


class TestHelperFunctions(unittest.TestCase):
    def test_get_plural_books(self):
        """Тест склонения слова \"книга\""""
        self.assertEqual(get_plural_books(1), "книга")
        self.assertEqual(get_plural_books(2), "книги")
        self.assertEqual(get_plural_books(5), "книг")
        self.assertEqual(get_plural_books(0), "книг")

    @patch("builtins.print")
    def test_print_table_of_books(self, mock_print):
        """Тест вывода таблицы книг"""
        Book(1, "Test Book", "Test Author", 2023)
        print_table_of_books(books)
        mock_print.assert_called()  # Проверяем, что print вызван



if __name__ == "__main__":
    unittest.main()
