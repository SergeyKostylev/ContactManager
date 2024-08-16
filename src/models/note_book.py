from collections import UserDict
from typing import Any

from src.services import storage_manager


class Notebook(UserDict):
    def __init__(self, __dict: None = None):
        super().__init__(__dict)
        self.STORAGE_FILE_NAME = "notebook.pkl"

    def get_all(self):
        """Get all records in dictionary format."""
        return self.data.values()

    def add_note(self, note):
        note_id = len(self.data) + 1
        self.data[note_id] = note

    def find_note(self, note):
        return self.data.get(note)
    
    def find_note_by_tag(self, tag):
        return [note for note in self.data.values() if tag in note.tags]
    
    def change_note(self, note, new_note):
        if note in self.data:
            self.data[note] = new_note
            return True
        return False

    def delete(self, note_id):
        if note_id in self.data:
            del self.data[note_id]

    def load_data(self):
        storage_manager.load(self, self.STORAGE_FILE_NAME)

    def save_data(self):
        storage_manager.save(self.data, self.STORAGE_FILE_NAME)


class Note:
    def __init__(self, content, tags=None):
        self.content = content
        self.tags = tags

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        tags_str = ", ".join(self.tags)
        return f"Note: {self.content}, Tags: {tags_str}"

    def to_dict(self):
        return {
            "content": self.content,
            "tags": ", ".join(self.tags),
        }

    
def add_note(args, notebook: Notebook):
    content, *tags = args
    note = Note(content, tags)
    notebook.add_note(note)
    return "Note added."


def find_note_by_tag(args, notebook: Notebook):
    tag, *_ = args
    notes = notebook.find_note_by_tag(tag)
    if not notes:
        return "No notes with such tag."
    return "\n".join(str(note) for note in notes)


def delete_note(args, notebook: Notebook):
    note_id, *_ = args
    notebook.delete(int(note_id))
    return "Note deleted."