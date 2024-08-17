from src.exeptions.exceptions import CancelInputCommandException
from src.exeptions.exceptions import ValidateException
from src.models.address_book import AddressBook
from src.models.note_book import Note, Notebook
from src.services.console_models_filler import fill_new_book_record, EMPTY_FIELD_COMMAND, CANCEL_FILLING_COMMAND, \
    fill_phone_number, fill_user_name, fill_address, fill_email, fill_birthdate, fill_days, fill_note, fill_title, fill_content, fill_tags
from src.services.pretty_output import ConsoleTextDesigner
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.styles import Style

class App:
    def __init__(self):
        self.__designer = ConsoleTextDesigner()
        self.notebook = Notebook()
        self.book = AddressBook()
        pass

    def run(self):
        self.book.load_data()
        self.notebook.load_data()

        commands = ["close","exit","hello","add","add_phone","change_phone","delete_phone",
                    "update_address","update_email","add_birthday","show_upcoming_birthday",
                    "all","show_by_name","show_by_part_name", "all_notes",
                    "add_note", "find_note_by_tag", "delete_note", "remove_contact", "change_content_by_title"]
        command_completer = WordCompleter(commands)
        session = PromptSession(completer=command_completer)
        style = Style.from_dict({'prompt': 'ansiblue'})
        self.__designer.print_info("Welcome to the assistant bot!")
        self.__designer.print_info("I’m your personal Contact Manager.\nI’ll help you easily create and manage contacts, including names, phone numbers and other details.\nYou can view, search, and edit contacts, add notes and tags.\nType 'help' to view all available commands.")

        while True:
            try:
                command = session.prompt('Enter a command: ', style = style)
                output = ''
                if command in ["close", "exit"]:
                    self.__designer.print_info("Good bye!")
                    break
                elif command == "help":
                    commands_list = "\n".join(commands)
                    self.__designer.print_info(f"Available commands:\n{commands_list}")
                elif command == "hello":
                    self.__designer.print_info("How can I help you?")
                elif command == "add":
                    self.command_control_tip()
                    person = fill_new_book_record()
                    if person is None:
                        continue
                    self.book.add_new_record(person)
                    output = f"{person.name} was added to the book."
                elif command == "remove_contact":
                    name = fill_user_name()
                    if self.book.delete(name):
                        output = "Contact was removed."
                elif command == "add_phone":
                    self.command_control_tip()
                    name = fill_user_name()
                    phone = fill_phone_number()
                    if self.book.add_new_phone(name, phone):
                        output = f"Phone {phone} was added for {name} user."
                elif command == "change_phone":
                    name = fill_user_name()
                    phone_old = fill_phone_number()
                    phone_new = fill_phone_number()
                    if self.book.change_phone(name, phone_old, phone_new):
                        output = f"Phone {phone_old} was changed to {phone_new} for {name} user."
                elif command == "delete_phone":
                    name = fill_user_name()
                    phone_to_delete = fill_phone_number()
                    if self.book.delete_phone(name, phone_to_delete):
                        output = "Phone was removed."
                elif command == "update_address":
                    name = fill_user_name()
                    address = fill_address()
                    if self.book.update_address(name, address):
                        output = "Address was updated."
                elif command == "update_email":
                    name = fill_user_name()
                    email = fill_email()
                    if self.book.update_email(name, email):
                        output = "Email was updated."
                elif command == "add_birthday":
                    name = fill_user_name()
                    birthdate = fill_birthdate()
                    if self.book.add_birthday(name, birthdate):
                        output = "Birthday was added."
                elif command == "show_upcoming_birthday":
                    shift_days = fill_days()
                    records = self.book.get_upcoming_birthdays(shift_days)
                    self.__designer.print_table(self.convert_records_to_dicts(records))
                elif command == "all":
                    records = list(self.book.get_all())
                    self.__designer.print_table(self.convert_records_to_dicts(records))
                elif command == "show_by_name":
                    name = fill_user_name()
                    record = self.book.get_by_name(name)
                    if record:
                        self.__designer.print_table(self.convert_records_to_dicts([record]))
                    else:
                        self.__designer.print_info("No record found.")
                elif command == "show_by_part_name":
                    part_name = self.__designer.print_input("Enter part of the name: ")
                    records = self.book.get_by_part_name(part_name)
                    self.__designer.print_table(self.convert_records_to_dicts(records))
                elif command == "add_note":
                    self.command_control_tip()
                    note = fill_note()
                    if note is None:
                        continue
                    self.notebook.add_note(note)
                    output = "Note was added."   
                elif command == "all_notes":
                    notes = self.notebook.get_all()
                    self.__designer.print_table(self.convert_records_to_dicts(notes))
                elif command == "find_note_by_tag":
                    self.command_control_tip()
                    self.__designer.print_info("Type a few tags that u want to search")
                    tags_to_search = fill_tags()
                    notes = self.notebook.find_note_by_tags(tags_to_search)
                    self.__designer.print_table(self.convert_records_to_dicts(notes))
                elif command == "find_note_by_keywords":
                    keyword = self.__designer.print_input("Type keyword: ")
                    notes = self.notebook.find_note_by_keywords(keyword)
                    self.__designer.print_table(self.convert_records_to_dicts(notes))
                elif command == "delete_note":
                    self.command_control_tip()
                    title = fill_title()
                    if self.notebook.delete_by_title(title):
                        self.__designer.print_info("Title was deleted")
                elif command == "change_content_by_title":
                    self.command_control_tip()
                    title = fill_title()
                    content = fill_content()
                    if self.notebook.change_content_by_title(title, content):
                        self.__designer.print_info("Content was changed")   
                else:
                    self.__designer.print_error("Invalid command.")

                if output != '':
                    self.__designer.print_info(output)
            
            except ValidateException as e:
                self.__designer.print_error(str(e))

            except CancelInputCommandException:
                pass

        self.book.save_data()
        self.notebook.save_data()



    def command_control_tip(self):
        self.__designer.print_info(f"Use '{EMPTY_FIELD_COMMAND}' for skip property and '{CANCEL_FILLING_COMMAND}' to cancel command")

    @staticmethod
    def convert_records_to_dicts(records):
        return [record.to_dict() for record in records]