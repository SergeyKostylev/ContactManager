class BookRecord:
    def __init__(self, name: str, email=None, phone_numbers=None, address=None, birth_date=None):
        self.__name = name
        self.__email = email
        self.__pone_numbers = [] if phone_numbers is None else phone_numbers
        self.__address = address
        self.__birth_date = birth_date

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def pone_numbers(self) -> list:
        return self.__pone_numbers

    @property
    def address(self) -> str:
        return self.__address

    @property
    def birth_date(self) -> str:
        return self.__birth_date
