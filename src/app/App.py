from src.models.address_book import AddressBook
from src.services.console_models_filler import fill_new_book_record, EMPTY_FIELD_COMMAND, CANCEL_FILLING_COMMAND, \
    fill_phone_number, fill_user_name, fill_address, fill_email, fill_birthdate
from src.services.pretty_output import ConsoleTextDesigner


class App:
    def __init__(self):
        self.__designer = ConsoleTextDesigner()
        pass

    def run(self):
        book = AddressBook()
        book.load_data()
        self.__designer.print_info("Welcome to the assistant bot!")

        while True:
            command = self.__designer.print_input("Enter a command: ")
            output = ''
            if command in ["close", "exit"]:
                self.__designer.print_info("Good bye!")
                break
            elif command == "hello":
                self.__designer.print_info("How can I help you?")
            elif command == "add":
                self.command_control_tip()
                person = fill_new_book_record()
                book.add_new_record(person)
            elif command == "add_phone":
                name = fill_user_name()
                phone = fill_phone_number()
                book.add_new_phone(name, phone)
            elif command == "change_phone":
                name = fill_user_name()
                phone_old = fill_phone_number()
                phone_new = fill_phone_number()
                book.change_phone(name, phone_old, phone_new)
            elif command == "delete_phone":
                name = fill_user_name()
                phone_to_delete = fill_phone_number()
                book.delete_phone(name, phone_to_delete)
            elif command == "update_address":
                name = fill_user_name()
                address = fill_address()
                book.update_address(name, address)
            elif command == "update_email":
                name = fill_user_name()
                email = fill_email()
                book.update_email(name, email)
            elif command == "add_birthday":
                name = fill_user_name()
                birthdate = fill_birthdate()
                book.add_birthday(name, birthdate)
            elif command == "show_upcoming_birthday":
                # book.get_upcoming_birthdays() TODO !!!!!!!
                pass
            elif command == "show_all":
                # book.get_all() TODO !!!!!!!
                pass
            elif command == "show_by_name":
                # book.get_by_name() TODO !!!!!!!
                pass
            elif command == "show_by_part_name":
                # book.get_by_part_name() TODO !!!!!!!
                pass
            # elif command == "add-note":
            #     print(add_note(args, notebook))

            # elif command == "find-note":
            #     print(find_note(args, notebook))

            # elif command == "delete-note":
            #     print(delete_note(args, notebook))

            # elif command == "add-birthday":
            #     print("Need to do.")
            # elif command == "show-birthday":
            #     print("Need to do.")
            # elif command == "birthdays":
            #     print("Need to do.")
            else:
                self.__designer.print_error("Invalid command.")

            self.__designer.print_info(output)

        book.save_data()



    def command_control_tip(self):
        self.__designer.print_info(f"Use '{EMPTY_FIELD_COMMAND}' for skip property and '{CANCEL_FILLING_COMMAND}' to cancel command")