import pickle


def load(self, filename: str):
    """Load data from a file for dict object instance."""
    try:
        with open(self.STORAGE_FILE_NAME, "rb") as file:
            self.data = pickle.load(file)
    except FileNotFoundError:
        self.data = {}


def save(data, filename: str):
    with open(filename, "wb") as file:
        pickle.dump(data, file)