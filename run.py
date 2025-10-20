from src.manager import Manager


def main():
    program_manager = Manager(base_dir="./files")
    while True:
        program_manager.show_options()
        command = int(input("> "))
        program_manager.menu(command)
        if command == 8:
            break


if __name__ == "__main__":
    main()
