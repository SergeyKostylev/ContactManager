import re
from datetime import datetime, timedelta

DATE_FORMAT = '%d.%m.%Y'

def validate_email(email: str) -> bool:
    email_regex = r"(^[\w\.-]+@[\w\.-]+\.\w+$)"
    return re.match(email_regex, email) is not None


def validate_address(address: str) -> bool:
    address_regex = r"^[\w\s\.,#-]+$"
    return re.match(address_regex, address) is not None


def validate_phone_number(phone_number: str) -> bool:
    phone_regex = r"^\d{10}$"
    return re.match(phone_regex, phone_number) is not None


def validate_user_name(user_name: str) -> bool:
    username_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['\-\s][A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    return re.match(username_regex, user_name) is not None

def validate_note_title(title: str) -> bool:
    length = len(title.strip())
    return length >= 3 and length <=10

def validate_note_content(content: str) -> bool:
    length = len(content.strip())
    return length >= 5 and length <=20


def validate_strings_with_tags(strings_with_tags: str):
    # Method receives raw string with tags. Example: "tag1 tag2 tag3". Must be separated by space.
    length = len(strings_with_tags.strip())
    return length > 0




def validate_shift_days(shift_days: str) -> bool:
    reg = r"^\d+$"
    return re.match(reg, shift_days) is not None

def validate_birthday(birthday: str) -> bool:
    try:
        birthday_date = datetime.strptime(birthday, DATE_FORMAT)
        # Get today's date
        today = datetime.today()

        if birthday_date > today:
            return False

        if birthday_date < today - timedelta(days=365 * 100):
            return False

        return True
    except ValueError:
        return False
