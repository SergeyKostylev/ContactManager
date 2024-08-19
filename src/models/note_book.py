from collections import UserDict
from src.exeptions.exceptions import ValidateException
from src.services import storage_manager
from src.services.error_handler import input_error


class Note:
    def __init__(self, title: str, content: str, tags=None):
        self.title = title
        self.content = content
        self.tags = tags if tags else []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        tags_str = ", ".join(self.tags)
        return f"Title: {self.title}, Content: {self.content}, Tags: {tags_str}"

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "tags": self.tags
        }


class Notebook(UserDict):
    def __init__(self, __dict: None = None):
        super().__init__(__dict)
        self.STORAGE_FILE_NAME = "notebook.pkl"

    def get_all(self):
        """Get all records in dictionary format."""
        return self.data.values()

    @input_error
    def add_note(self, note: Note):
        title = note.title.lower()
        if title in self.data:
            raise ValidateException(f"Note '{note.title}' already exist.")
        self.data[title] = note
        return True

    @input_error
    def find_note_by_title(self, title: str) -> Note:
        return self.data.get(title.lower())

    def find_note_by_tags(self, tags_to_search: list):
        result = {}
        for tag in tags_to_search:
            for note in self.data.values():
                if tag in note.tags:
                    result[note.title] = note
        return result.values()

    def find_note_by_keywords(self, keyword: str):
        result = {}
        keyword = keyword.lower().strip()
        if keyword == '':
            return []

        for note in self.data.values():
            title = note.title.lower()
            content = note.content.lower()
            if keyword in title or keyword in content:
                result[note.title] = note
                continue
            for tag in [s.lower() for s in note.tags]:
                if keyword in tag:
                    result[note.title] = note

        return result.values()

    @input_error
    def change_content_by_title(self, title: str, content: str):
        title_key = title.lower()
        if title_key in self.data:
            self.data[title_key].content = content
        else:
            raise ValidateException(f"Note with title '{title}' was not found.")
        return True

    @input_error
    def change_tags_by_title(self, title: str, tags: list):
        title_key = title.lower()
        if title_key in self.data:
            self.data[title_key].tags = tags
        else:
            raise ValidateException(f"Note with title '{title}' was not found.")
        return True

    @input_error
    def delete_by_title(self, title: str):
        title_key = title.lower()
        if title_key in self.data:
            self.data.pop(title_key)
        else:
            raise ValidateException(f"Note with title '{title}' was not found.")
        return True

    def load_data(self):
        storage_manager.load(self, self.STORAGE_FILE_NAME)

    def save_data(self):
        storage_manager.save(self.data, self.STORAGE_FILE_NAME)
