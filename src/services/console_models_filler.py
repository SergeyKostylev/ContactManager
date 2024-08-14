from src.services.validator import validate_user_name, validate_phone_number
from src.services.pretty_output import ConsoleTextDesigner as designer


EMPTY_FIELD_COMMAND = 'n'
FINISH_FILLING_COMMAND = 'stop'


def fill_new_book_record():

    properties = [
        "name",
        "email",
        "phone_numbers",
        "address",
        "birth_date"
    ]

    name = None
    email = None
    phone_numbers = None
    address = None
    birth_date = None

    while True:
        if len(properties) == 0:
            break

        prop = properties[0]

        if prop == "name":
            name_candidate = test_call_back("print name: ", validate_user_name, "name is not valid")
            if name_candidate is not False:
                name = name_candidate
            else:
                continue


        if prop == "phone_numbers":
            input_phones = input("print phone: ")
            if not validate_phone_number(input_phones):
                print("phone is not valid")
                continue
            phone_numbers = input_phones

        properties.pop(0)



    print('__________')
    print(name, phone_numbers)
    print('__________')

def test_call_back(input_message: str, validate_function, wrong_message):
    input_value = designer().print_info(input_message)
    if not validate_function(input_value):
        designer().print_warning(wrong_message)
        return False

    return input_value
