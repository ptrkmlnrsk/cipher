from src.manager import Menu


def main():
    menu = Menu()
    while True:
        menu.show_options()
        command = int(input("> "))
        menu.menu_handler(command)
        if command == 8:
            break


if __name__ == "__main__":
    main()
