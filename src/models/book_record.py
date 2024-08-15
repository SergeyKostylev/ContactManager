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
    def pone_numbers(self) -> list:
        return self.__pone_numbers

    @pone_numbers.setter
    def pone_numbers(self, pone_numbers):
        self.__pone_numbers = pone_numbers

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