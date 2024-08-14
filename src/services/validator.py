import re
from src.services.console_text_designer import ConsoleTextDesigner as console_des
from datetime import datetime, timedelta

def email(email: str) -> bool:
    email_regex = r"(^[\w\.-]+@[\w\.-]+\.\w+$)"
    return re.match(email_regex, email) is not None


def address(address: str) -> bool:
    address_regex = r"^[\w\s\.,#-]+$"
    return re.match(address_regex, address) is not None


def validate_phone_number(phone_number: str) -> bool:
    phone_regex = r"^\d{10}$"
    return re.match(phone_regex, phone_number) is not None


def validate_user_name(user_name: str) -> bool: 
    username_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:['\-\s][A-Za-zÀ-ÖØ-öø-ÿ]+)*$"
    return re.match(username_regex, user_name) is not None


def validate_birthday(birthday: str) -> bool:
    # DD.MM.YYYY
    birthday_regex = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"
    
  
    if not re.match(birthday_regex, birthday):
        return False
    
    try:
        
        birthday_date = datetime.strptime(birthday, '%d.%m.%Y')
        
        # Get today's date
        today = datetime.today()
            
        if birthday_date > today:
            return False
            
        if birthday_date < today - timedelta(days=365*100):
            return False
        
        return True
    except ValueError:
        return False