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



class Book:
    """Класс книги"""

    id: int
    title: str
    author: str
    year: int
    status: str

    def __init__(self, title: str, author: str, year: int):
        self.id = len(books)
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

        books.append(self)



def help() -> None:
    """Выводит список доступных команд"""

    print("Доступные команды (вводить можно как на английском, так и на русском):")
    for c in documentation.keys():
        print(c, "\t", documentation[c], sep="")


def add() -> None:
    """Запрашивает у пользователя параметры книги и добавляет её в систему"""

    title = input("Название книги: ")
    author = input("Автор: ")
    year = input("Год издания: ")

    Book(title, author, year)


def main() -> None:
    """Основная функция приложения"""

    print("Добро пожаловать в систему управления библиотекой \"USLib\"!")
    print("Введите \"помощь\" для вывода всех доступных команд")

    while True:
        command: list = input("> ")
        if command:
            match command.lower():
                case "help" | "помощь":
                    help()
                case "add" | "добавить":
                    add()
                case "del" | "удалить":
                    delete()
                case "find" | "найти":
                    find()
                case "list" | "список":
                    show_list()
                case "status" | "статус":
                    status()
                case "exit" | "выход":
                    break
                case _:
                    print("Такой команды не существует")
            print()



if __name__ == "__main__":
    main()