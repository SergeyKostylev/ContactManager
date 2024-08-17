from src.exeptions.exceptions import ValidateException, CancelInputCommandException
from src.models.book_record import BookRecord
from src.services.error_handler import input_error
from src.services.validator import validate_user_name, validate_phone_number, validate_email, validate_address, \
    validate_birthday, validate_shift_days, validate_note_title, validate_note_content, validate_strings_with_tags
from src.services.pretty_output import ConsoleTextDesigner as designer
from src.models.note_book import Note

EMPTY_FIELD_COMMAND = 'n'
CANCEL_FILLING_COMMAND = 'cancel'

@input_error
def fill_new_book_record():
    properties = [
        "name",
        "email",
        "phone_numbers",
        "address",
        "birth_date"
    ]

    name = None
    phone_numbers = None
    email = None
    address = None
    birthdate = None

    while True:
        if len(properties) == 0:
            break

        prop = properties[0]

        match prop:
            case "name":
                name = fill_user_name()
                if name is None:
                    raise ValidateException('User name cannot be empty.')
            case "phone_numbers":
                phone_number = fill_phone_number()
                phone_numbers = [] if phone_number is None else [phone_number]
            case "email":
                email = fill_email()
            case "address":
                address = fill_address()
            case "birth_date":
                birthdate = fill_birthdate()

        properties.pop(0)

    return BookRecord(name, email, phone_numbers, address, birthdate)

@input_error
def fill_note():
    properties = [
        "title",
        "content",
        "tags"
    ]

    title = None
    content = None
    tags = []

    while True:
        if len(properties) == 0:
            break

        prop = properties[0]

        match prop:
            case "title":
                title = fill_title()
                if title is None:
                    raise ValidateException('Title cannot be empty.')
            case "content":
                content = fill_content()
                if content is None:
                    raise ValidateException('Content cannot be empty.')
            case "tags":
                tags = fill_tags()
    

        properties.pop(0)

    return Note(title, content, tags)
    

def fill_days():
    while True:
        days = input_data(f"Enter the number of days: ", validate_shift_days, "Days must be a positive integer.")
        if days is not False:
            return int(days)

def fill_birthdate():
    while True:
        birthday = input_data(f"Print birthdate with format d.m.y: ", validate_birthday, "Birthdate is not valid.")
        if birthday is not False:
            return birthday

def fill_address():
    while True:
        address = input_data(f"Print address: ", validate_address, "Address is not valid.")
        if address is not False:
            return address

def fill_email():
    while True:
        email = input_data(f"Print email: ", validate_email, "Email is not valid.")
        if email is not False:
            return email


def fill_phone_number():
    while True:
        phone_number = input_data(f"Print phone number: ", validate_phone_number, "Phone is not valid.")
        if phone_number is not False:
            return phone_number


def fill_user_name():
    while True:
        name = input_data("Print user name: ", validate_user_name, "Name is not valid.")
        if name is None:
            designer().print_warning("User name cannot be empty.")
            continue
        if name is not False:
            return name
        
def fill_title():
    while True:
        title = input_data("Print title: ", validate_note_title, "Title must be more than 3 and less than 10 characters.")
        if title is None:
            designer().print_warning("Title cannot be empty.")
            continue
        if title is not False:
            return title
        
def fill_content():
    while True:
        content = input_data("Print content: ", validate_note_content, "Content must be more than 5 and less than 20 characters.")
        if content is None:
            designer().print_warning("Content cannot be empty.")
            continue
        if content is not False:
            return content
        
def fill_tags():
    while True:
       strings_with_tags = input_data("Print tags(separated by space): ", validate_strings_with_tags, "Tags must not be empty") 
       if strings_with_tags is None:
            return []
       if strings_with_tags is not False:
            result = []
            for tag_candidate in strings_with_tags.split(" "):
                if len(tag_candidate) > 0:
                    result.append(tag_candidate.strip().lower())
            return list(set(result))




def input_data(input_message: str, validate_function, wrong_message) -> str | None | bool:
    input_value = designer().print_input(input_message)
    if input_value == EMPTY_FIELD_COMMAND:
        return None

    if input_value == CANCEL_FILLING_COMMAND:
        raise CancelInputCommandException('Command was cancelled.')

    if not validate_function(input_value):
        designer().print_warning(wrong_message)
        return False

    return input_value
