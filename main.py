import json



documentation: dict = {
    "help / помощь": "Вывести список доступных команд",
    "add / добавить": "Добавить новую книгу",
    "del / удалить": "Удалить книгу",
    "find / найти": "Найти книгу",
    "list / список": "Вывести список всех книг",
    "status / статус": "Установить статус книги (в наличии/выдана)"
}



def help(command: str = "") -> None:
    """Выводит список доступных команд"""

    if not command:
        print("Доступные команды (вводить можно как на английском, так и на русском):")
        for c in documentation.keys():
            print(c, "\t", documentation[c], sep="")
    print()


def main() -> None:
    """Основная функция приложения"""

    print("Добро пожаловать в систему управления библиотекой \"USLib\"!")
    print("Введите \"помощь\" для вывода всех доступных команд")
    print()

    while True:
        command: list = input("> ").split(" ")
        if command:
            match command[0].lower():
                case "help" | "помощь":
                    help()



if __name__ == "__main__":
    main()