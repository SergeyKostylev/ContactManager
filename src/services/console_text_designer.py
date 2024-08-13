from colorama import Fore, Back, Style


class ConsoleTextDesigner:
    def print_input(self, message):
        return input(Fore.WHITE + message + Style.RESET_ALL)

    def print_output(self, message):
        self.__print(Fore.BLUE + message)

    def print_error(self, message):
        self.__print(Fore.RED + message)

    def print_warning(self, message):
        self.__print(Fore.YELLOW + message)

    def print_info(self, message):
        self.__print(Fore.CYAN + message)

    def print_table(self, list_of_dict_to_display, displayed_columns=None):
        # TODO need tabulate and colorama
        pass

    def __print(self, message):
        print(message + Style.RESET_ALL)
