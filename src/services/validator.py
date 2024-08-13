import re
from src.services.console_text_designer import ConsoleTextDesigner as console_des


BIRTHDAY_FORMAT = "%Y-%m-%d"

def email(email: str) -> bool:
    # TODO: add validation
    pass


def address(address: str) -> bool:
    # TODO: add validation
    pass



def validate_phone_number(phone_number: str) -> bool:
    if not re.fullmatch(r'^\d{3}$', phone_number):  # TODO 3 -> 10
        console_des.print_warning('ERROR') # TODO describe error message
        return False
    return True


def validate_user_name(user_name: str) -> bool:  # TODO: edit validation
    if len(user_name) < 3:
        return False

    return True


def birthday(birthday: str) -> bool:

    # TODO: add validation (use constant BIRTHDAY_FORMAT)
    # check the date that it is not older than today and not more than 100 years
    pass
