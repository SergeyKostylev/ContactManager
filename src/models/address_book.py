from collections import UserDict

from src.exeptions.exceptions import ValidateException
from src.models.book_record import BookRecord
from datetime import datetime
from src.services import storage_manager

from src.services.error_handler import input_error


class AddressBook(UserDict):
    STORAGE_FILE_NAME = "addressbook.pkl"

    def get_all(self) -> dict[BookRecord, BookRecord]:
        """Get all records."""
        return self.data.values()

    @input_error
    def get_by_name(self, name: str) -> dict[BookRecord] | None:
        """Get a record by exact name or return None if not found."""
        return self.data.get(name)

    @input_error
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

    @input_error
    def delete(self, name: str) -> bool:
        """Delete a record by name."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        self.data.pop(name)
        return True

    def update_record(self, name: str, new_record: BookRecord) -> bool:
        """Update an existing record."""
        if name in self.data:
            self.data.pop(name)
            self.data[new_record.name] = new_record
            return True
        return False

    @input_error
    def get_upcoming_birthdays(self, days: int) -> list[BookRecord]:
        """Method to get upcoming birthdays"""
        today = datetime.now().date()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birth_date:
                birth_date = datetime.strptime(record.birth_date, "%d.%m.%Y").date()
                next_birthday = birth_date.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)
                if 0 <= (next_birthday - today).days <= days:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

    @input_error
    def add_new_phone(self, name: str, phone_number: str) -> bool:
        """Add new phone number to contact."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        if phone_number in record.phone_numbers:
            raise ValidateException(f"Phone number '{phone_number}' already exist for name '{name}'.")
        record.phone_numbers.append(phone_number)
        return True

    @input_error
    def change_phone(self, name: str, old_phone_number: str, new_phone_number: str) -> bool:
        """Change an existing phone number to a new one."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        if old_phone_number not in record.phone_numbers:
            raise ValidateException(f"Phone number '{old_phone_number}' does not exist for '{name}'.")
        record.phone_numbers.remove(old_phone_number)
        record.phone_numbers.append(new_phone_number)
        return True

    @input_error
    def delete_phone(self, name: str, phone_to_delete: str) -> bool:
        """Delete a phone number from a contact."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        if phone_to_delete not in record.phone_numbers:
            raise ValidateException(f"Phone number '{phone_to_delete}' does not exist for '{name}'.")
        record.phone_numbers.remove(phone_to_delete)
        return True

    @input_error
    def update_address(self, name: str, new_address: str) -> bool:
        """Update the address of a contact."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        record.address = new_address
        return True

    @input_error
    def update_email(self, name: str, email: str) -> bool:
        """Update the email of a contact."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        record.email = email
        return True

    @input_error
    def add_birthday(self, name: str, birthday: str) -> bool:
        """Add a birthday to a contact."""
        record = self.get_by_name(name)
        if not record:
            raise ValidateException(f"Record with name '{name}' does not exist.")
        if record.birth_date:
            raise ValidateException(f"Birthday already set for '{name}'.")
        record.birth_date = birthday
        return True

    def load_data(self):
        """Load address book data from a file."""
        storage_manager.load(self, self.STORAGE_FILE_NAME)

    def save_data(self):
        """Save address book data to a file."""
        storage_manager.save(self.data, self.STORAGE_FILE_NAME)
