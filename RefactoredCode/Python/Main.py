from RefactoredCode.Python.UserInterface import UserInterface


def main():
    user_interface = UserInterface()

    user_interface.read_user_data()
    user_interface.print_user_taxes()


if __name__ == '__main__':
    main()
