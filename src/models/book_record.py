class BookRecord:

    def __init__(self, name: str, email=None, phone_numbers=None, address=None, birth_date=None):
        self.__name = name
        self.__email = email
        self.__phone_numbers = [] if phone_numbers is None else phone_numbers
        self.__address = address
        self.__birth_date = birth_date

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def phone_numbers(self) -> list:
        return self.__phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        self.__phone_numbers = phone_numbers

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def birth_date(self) -> str:
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self.__birth_date = birth_date

    def to_dict(self):
        return {
            "name": self.name,
            "phones": self.__phone_numbers,
            "address": self.address,
            "birth_date": self.birth_date,
            "email": self.email,
        }
