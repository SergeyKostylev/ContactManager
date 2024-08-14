from rich.console import Console
from rich.table import Table


class ConsoleTextDesigner:
    COLUMN_COLORS = {
        1: "cyan",
        2: "green",
        3: "yellow",
        4: "blue",
        5: "magenta",
        6: "red",
        7: "purple",
        8: "orange",
        9: "pink",
        10: "white",
        11: "bright_cyan",
        12: "bright_green",
        13: "bright_yellow",
        14: "bright_blue",
        15: "bright_magenta",
        16: "bright_red",
        17: "bright_purple",
        18: "bright_orange",
        19: "bright_pink",
        20: "bright_white"
    }

    def __init__(self):
        self.console = Console()

    def print_with_color(self, message: str, color: str):
        self.console.print(message, style=color)

    def print_error(self, message: str):
        self.print_with_color(message, "bold red")

    def print_warning(self, message: str):
        self.print_with_color(message, "bold orange3")

    def print_info(self, message: str):
        self.print_with_color(message, "bold green")

    def print_result(self, message: str):
        self.print_with_color(message, "bold blue")


    def print_table(self, list_of_dict_to_display, displayed_columns=None):
        table = Table(show_header=True, header_style="bold magenta")

        if not list_of_dict_to_display:
            self.console.print("No data to display", style="bold red")
            return

        columns = displayed_columns or list_of_dict_to_display[0].keys()
        for index, column in enumerate(columns, start=1):
            color = self.COLUMN_COLORS.get(index, "white")
            table.add_column(column, style=color)

        for item in list_of_dict_to_display:
            row = [str(item.get(column, "")) for column in columns]
            table.add_row(*row)

        self.console.print(table)

