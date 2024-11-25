from datetime import datetime
import json



documentation: dict = {  # Описания команд
    "help / помощь": "Вывести список доступных команд",
    "add / добавить": "Добавить новую книгу",
    "del / удалить": "Удалить книгу",
    "find / найти": "Найти книгу",
    "list / список": "Вывести список всех книг",
    "status / статус": "Установить статус книги (в наличии/выдана)",
    "exit / выход": "Выйти из приложения"
}

books: list = []  # Список со всеми книгами в системе

last_id: int = 0  # ID, данное последней добавленной книге



class Book:
    """Класс книги"""

    id: int
    title: str
    author: str
    year: int
    status: str

    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        """Создаёт объект книги"""
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

        books.append(self)
    
    def to_dict(self) -> dict:
        """Превращает объект в словарь для сериализации"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        """Превращает словарь в объект книги"""
        return cls(
            data["id"],
            data["title"],
            data["author"],
            data["year"],
            data["status"]
        )



def save_data(file_name: str = "data.json") -> None:
    """Сохраняет базу книг в файл"""

    try:
        data: dict = {
            "last_save_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_id": last_id,
            "books": [book.to_dict() for book in books]
        }

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except:
        print("Сохранить базу не удалось!")


def load_data(file_name: str = "data.json") -> None:
    """Загружает базу книг из файла"""

    global last_id

    try:
        data: dict = {}

        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        
        last_id = data["last_id"]
        books = [Book.from_dict(book) for book in data["books"]]
    except FileNotFoundError:
        pass
    except:
        print("Загрузка базы не удалась!")


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

    print("  ID |           Название           |           Автор           | Год |  Статус ")
    print("-----+------------------------------+---------------------------+-----+---------")

    for b in list_of_books:
        print(str(b.id).rjust(5),
            b.title.center(30),
            b.author.center(27),
            str(b.year).rjust(5),
            b.status.center(9),
            sep="|")


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
        save_data()
        print(f"Книга \"{title}\" успешно добавлена в систему под ID {last_id}")
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
                save_data()
                print(f"Книга \"{deleted_book.title}\" успешно удалена из системы")
                break
        if not deleted_book:
            print("Книга с указанным ID не найдена")
    else:
        print("ID введён некорректно (должно быть целое число не меньше нуля)")



def find_books() -> None:
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
                if title.lower() in b.title.lower():
                    matched_books.append(b)
            if matched_books:
                print(f"В библиотеке {len(matched_books)} {get_plural_books(len(matched_books))} с похожим названием:")
            else:
                print("Книг с данным названием не найдено")

        case "2" | "author" | "автор" | "2 - автор":
            author: str = input("Введите автора книги: ")
            for b in books:
                if author.lower() in b.author.lower():
                    matched_books.append(b)
            if matched_books:
                print(f"В библиотеке {len(matched_books)} {get_plural_books(len(matched_books))} с похожим автором:")
            else:
                print("Книг с данным автором не найдено")

        case "3" | "year" | "год" | "год издания" | "3 - год издания":
            year: str = input("Введите год издания книги: ")
            if year.isdecimal():
                for b in books:
                    if b.year == int(year):
                        matched_books.append(b)
                if matched_books:
                    print(f"В библиотеке {len(matched_books)} {get_plural_books(len(matched_books))} с данным годом:")
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
                        save_data()
                        print("Статус успешно изменён на \"в наличии\"")
                        break

                    case "2" | "checked out" | "выдана" | "2 - выдана":
                        b.status = "выдана"
                        save_data()
                        print("Статус успешно изменён на \"выдана\"")
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
    load_data()
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
                    find_books()
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
