from src.exeptions.exceptions import ValidateException, CancelInputCommandException
from src.services.pretty_output import ConsoleTextDesigner


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError, ValidateException) as e:
            ConsoleTextDesigner().print_error(f"Error: {str(e)}")
            return None
        except CancelInputCommandException as e:
            ConsoleTextDesigner().print_warning("Command was cancelled")

    return inner