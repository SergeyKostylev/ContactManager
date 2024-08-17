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
            "tags": ", ".join(self.tags)
        }


class Notebook(UserDict):
    def __init__(self, __dict: None = None):
        super().__init__(__dict)
        self.STORAGE_FILE_NAME = "notebook.pkl"

    def get_all(self):
        """Get all records in dictionary format."""
        return self.data.values()


    def add_note(self, note: Note):
        if note.title in self.data:
            raise ValidateException(f"Record with name '{note.title}' already exist.")
        self.data[note.title] = note
        return True
    

    def find_note_by_title(self, title: str) -> Note:
        return self.data.get(title)


    def find_note_by_tags(self, tags_to_search: list):
        result = {}
        for tag in tags_to_search:
            for note in self.data.values():
                if tag in note.tags:
                    result[note.title] = note
        return result.values()
    
    def find_note_by_keywords(self, keyword: str):
        result = {}
        # Перебрати всі note і перевірити чи keyword або title, content або хоча б водному з тегів то повертаємо result.values. 
        # for. якщо є в title, content continue
        return result.values()
    
    @input_error
    def change_content_by_title(self, title: str, content: str):
        if title in self.data:
            self.data[title].content = content
        else:
            raise ValidateException(f"Note with title '{title}' was not found.")
        return True
        

    @input_error
    def delete_by_title(self, title: str):
        if title in self.data:
            self.data.pop(title)
        else:
            raise ValidateException(f"Note with title '{title}' was not found.")
        return True


    def load_data(self):
        storage_manager.load(self, self.STORAGE_FILE_NAME)

    def save_data(self):
        storage_manager.save(self.data, self.STORAGE_FILE_NAME)


def add_note(args, notebook: Notebook):
    title, content, *tags = args
    note = Note(title, content, tags)
    notebook.add_note(note)
    return "Note added."


def delete_note(args, notebook: Notebook):
    title, *_ = args
    notebook.delete_by_title(title)
    return "Note deleted."


def find_note_by_tag(args, notebook: Notebook):
    tag, *_ = args
    notes = notebook.find_note_by_tag(tag)
    if not notes:
        return "No notes with such tag."
    return "\n".join(str(note) for note in notes)