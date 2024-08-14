from collections import UserDict

from src.exeptions.exceptions import ValidateException
from src.models.book_record import BookRecord
from datetime import datetime
import pickle

from src.services.error_handler import input_error


class AddressBook(UserDict):

    def get_all(self) -> dict[BookRecord, BookRecord]:
        """Get all records in dictionary format."""
        return self.data.values()

    def get_by_name(self, name: str) -> dict[BookRecord] | None:
        """Get a record by exact name or return None if not found."""
        return self.data.get(name)

    def get_by_part_name(self, part_name: str) -> list[BookRecord]:
        """Get records that contain part of the name."""
        return [record for name, record in self.data.items() if part_name.lower() in name.lower()]

    @input_error
    def add_new_record(self, book_record: BookRecord) -> bool:
        """Add a new record if it does not exist."""
        if book_record.name in self.data:
            raise ValidateException(f"Record with name '{book_record.name}' already exist.")
        self.data[book_record.name] = book_record
        return True

    def delete(self, name: str) -> bool:
        """Delete a record by name."""
        if name in self.data:
            self.data.pop(name)
            return True
        return False
    
    # TODO: wrong logic need to remove this method
    # Example if old name was AAA and new_record has nam BBB we save in the book wrong info {"AAA": <record with name BBB>}
    def update_record(self, name: str, new_record: BookRecord) -> bool:
        """Update an existing record."""
        if name in self.data:
            self.data[name] = new_record
            return True
        return False
    
    def get_upcoming_birthdays(self, days: int) -> list[BookRecord]:
        """Method to get upcoming birthdays"""
        today = datetime.now().date()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)
                if 0 <= (next_birthday - today).days <= days:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

    @input_error
    def add_new_phone(self, name: str, phone_number: str) -> bool:
        # TODO: search record by name. if name does not exist  raise ValidateException()
        #  if exist passed number in person not need to add twice
        pass

    @input_error
    def change_phone(self, name: str, old_phone_number: str, new_phone_number: str) -> bool:
        # TODO: search record by name. if name does not exist  raise ValidateException()
        #  if passed number does not exist  raise ValidateException()
        # ...
        pass

    @input_error
    def delete_phone(self, name: str, phone_to_delete: str) -> bool:
        # TODO: search record by name. if name does not exist  raise ValidateException()
        #  if passed number does not exist  raise ValidateException()
        # ...
        pass

    @input_error
    def update_address(self, name: str, new_address: str) -> bool:
        # TODO: search record by name. if name does not exist  raise ValidateException()
        #  set new address
        # ...
        pass

    @input_error
    def update_email(self, name: str, email: str) -> bool:
        # TODO: search record by name. if name does not exist  raise ValidateException()
        #  set new email
        # ...
        pass

    def add_birthday(self, name: str, birthday: str) -> bool:
        # TODO: search record by name. if name does not exist  raise ValidateException()
        #  if birthday already set  raise ValidateException()
        # ...
        pass

    def load_data(self, filename="addressbook.pkl"):
        """Load address book data from a file."""
        try:
            with open(filename, "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_data(self, filename="addressbook.pkl"):
        """Save address book data to a file."""
        with open (filename, "wb") as file:
            pickle.dump(self.data, file)