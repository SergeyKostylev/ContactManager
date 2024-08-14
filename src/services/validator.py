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
