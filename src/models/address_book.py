from collections import UserDict
from src.models.book_record import BookRecord
from datetime import datetime
import pickle

class AddressBook(UserDict):

    def get_all(self) -> dict[BookRecord, BookRecord]:
        """Get all records in dictionary format."""
        return self.data.values()

    def get_by_name(self, name: str) -> dict[BookRecord] | None:
        """Get a record by exact name or return None if not found."""
        return self.data.get(name)

    # TODO: other getters by task

    def get_by_part_name(self, part_name: str) -> list[BookRecord]:
        """Get records that contain part of the name."""
        return [record for name, record in self.data.items() if part_name.lower() in name.lower()]

    def add_new_record(self, book_record: BookRecord) -> bool:
        """Add a new record if it does not exist."""
        if book_record.name in self.data:
            return False
        self.data[book_record.name] = book_record
        return True

    def delete(self, name: str) -> bool:
        """Delete a record by name."""
        if name in self.data:
            self.data.pop(name)
            return True
        return False
    
    
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