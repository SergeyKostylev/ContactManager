from src.exeptions.exceptions import ValidateException
from src.services.pretty_output import ConsoleTextDesigner


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, ValidateException) as e:
            ConsoleTextDesigner().print_error(f"Error: {str(e)}")

    return inner