class BookRecord:
    def __init__(self, name: str, email=None, phone_numbers=None, address=None, birth_date=None):
        if phone_numbers is None:
            phone_numbers = []

        self.__name = name
        self.__email = email
        self.__pone_numbers = [] if phone_numbers is None else phone_numbers
        self.__address = address
        self.__birth_date = birth_date

    def is_valid(self) -> bool:
        return False

    # TODO: add getters and setters
