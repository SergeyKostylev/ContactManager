from collections import UserDict

from src.models.book_record import BookRecord


class AddressBook(UserDict):

    def get_all(self) -> dict[BookRecord, BookRecord]:
        return self.data.values()

    def get_by_name(self, name: str) -> dict[BookRecord, BookRecord]:
        # TODO: get by name or return None
        pass

    # TODO: other getters by task

    def get_by_part_name(self, name: str):
        # TODO: get by part name or return None
        pass

    def add_new_record(self, book_record: BookRecord) -> bool:
        # TODO: check to exist and add if it does not exist
        pass

    def delete(self, name) -> bool:
        res = False
        if name in self.data:
            self.data.pop(name)
            res = True

        return res

    def load_data(self):
        pass

    def save_data(self):
        pass