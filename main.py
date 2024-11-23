import json



documentation: dict = {
    "help / помощь": "Вывести список доступных команд",
    "add / добавить": "Добавить новую книгу",
    "del / удалить": "Удалить книгу",
    "find / найти": "Найти книгу",
    "list / список": "Вывести список всех книг",
    "status / статус": "Установить статус книги (в наличии/выдана)",
    "exit / выход": "Выйти из приложения"
}

books: list = []

last_id: int = 0



class Book:
    """Класс книги"""

    id: int
    title: str
    author: str
    year: int
    status: str

    def __init__(self, id: int, title: str, author: str, year: int):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

        books.append(self)



def get_plural_books(number: int) -> str:
    """Возвращает слово "книга" в указанном числе"""

    if number == 1:
        return "книга"
    elif 1 < number < 5:
        return "книги"
    else:
        return "книг"


def print_table_of_books(list_of_books: list) -> None:
    """Выводит переданный список книг в виде красивой таблицы"""

    for b in list_of_books:
        print(b.id, b.title, b.author, b.year, b.status, sep="\t")


def help() -> None:
    """Выводит список доступных команд"""

    print("Доступные команды (вводить можно как на английском, так и на русском):")
    for c in documentation.keys():
        print(c, "\t", documentation[c], sep="")


def add_book() -> None:
    """Запрашивает у пользователя параметры книги и добавляет её в систему"""

    global last_id

    title: str = input("Название книги: ")
    author: str = input("Автор: ")
    year: str = input("Год издания: ")

    if title and author and year.isdecimal():
        Book(last_id+1, title, author, int(year))
        last_id += 1
        print(f"Книга \"{title}\" успешно добавлена в систему")
    else:
        print("Необходимо корректно заполнить все поля, книга не добавлена")


def delete_book() -> None:
    """Запрашивает у пользователя id книги и удаляет её"""
    
    deleted_book: Book = None
    book_id: str = input("ID удаляемой книги: ")

    if book_id.isdecimal():
        for i, b in enumerate(books):
            if b.id == int(book_id):
                deleted_book = books.pop(i)
                print(f"Книга \"{deleted_book.title}\" успешно удалена из системы")
                break
        if not deleted_book:
            print("Книга с указанным ID не найдена")
    else:
        print("ID введён некорректно (должно быть целое число не меньше нуля)")



def find_book() -> None:
    """Запрашивает по какому параметру искать, затем сам параметр, после чего выводит подходящие книги"""

    print("Выберите, по какому параметру искать книги:")
    print("1 - Название")
    print("2 - Автор")
    print("3 - Год издания")
    param: str = input("Параметр: ").lower()

    matched_books: list = []

    match param:
        case "1" | "title" | "название" | "1 - название":
            title: str = input("Введите название книги: ")
            for b in books:
                if b.title == title:
                    matched_books.append(b)
            if matched_books:
                print(f"Найдено {len(matched_books)} {get_plural_books(len(matched_books))} с данным названием:")
            else:
                print("Книг с данным названием не найдено")

        case "2" | "author" | "автор" | "2 - автор":
            author: str = input("Введите автора книги: ")
            for b in books:
                if b.author == author:
                    matched_books.append(b)
            if matched_books:
                print(f"Найдено {len(matched_books)} {get_plural_books(len(matched_books))} с данным автором:")
            else:
                print("Книг с данным автором не найдено")

        case "3" | "year" | "год" | "год издания" | "3 - год издания":
            year: str = input("Введите год издания книги: ")
            if year.isdecimal():
                for b in books:
                    if b.year == int(year):
                        matched_books.append(b)
                if matched_books:
                    print(f"Найдено {len(matched_books)} {get_plural_books(len(matched_books))} с данным годом:")
                else:
                    print("Книг с данным годом не найдено")
            else:
                print("Год введён некорректно")

        case _:
            print("Неизвестный параметр")

    if matched_books:
        print_table_of_books(matched_books)


def show_list() -> None:
    """Выводит таблицу со всеми книгами в системе"""

    if books:
        print(f"В данный момент в системе {len(books)} {get_plural_books(len(books))}:")
        print_table_of_books(books)
    else:
        print("Сейчас в системе нет книг")


def set_book_status() -> None:
    """Запрашивает id книги, затем позволяет установить её статус (в наличии/выдана)"""

    book_id: str = input("ID взятой/возвращённой книги: ")

    if book_id.isdecimal():
        for b in books:
            if b.id == int(book_id):
                print(f"Выберите статус для \"{b.title}\" (сейчас {b.status}):")
                print("1 - В наличии")
                print("2 - Выдана")
                status: str = input("Статус: ").lower()
                match status:
                    case "1" | "available" | "в наличии" | "1 - в наличии":
                        b.status = "в наличии"
                        print("Статус успешно изменён")
                        break

                    case "2" | "checked out" | "выдана" | "2 - выдана":
                        b.status = "выдана"
                        print("Статус успешно изменён")
                        break

                    case _:
                        print("Можно установить только статус \"в наличии\" или \"выдана\"")
        else:
            print("Книга с указанным ID не найдена")
    else:
        print("ID введён некорректно (должно быть целое число не меньше нуля)")


def main() -> None:
    """Основная функция приложения"""

    print("Добро пожаловать в систему управления библиотекой \"USLib\"!")
    print("Введите \"помощь\" для вывода всех доступных команд")

    while True:
        command: str = input("> ").lower().strip()
        if command:
            match command:
                case "help" | "помощь":
                    help()
                case "add" | "добавить":
                    add_book()
                case "del" | "удалить":
                    delete_book()
                case "find" | "найти":
                    find_book()
                case "list" | "список":
                    show_list()
                case "status" | "статус":
                    set_book_status()
                case "exit" | "выход":
                    break
                case _:
                    print("Такой команды не существует")
            print()



if __name__ == "__main__":
    main()