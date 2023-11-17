import re
import os


def insert_text_into_file(file_path, text, pattern):
    with open(file_path, "a") as file:
        if re.match(pattern, text):
            file.write(text)
        else:
            file.write("None")


if __name__ == "__main__":
    new_file_path = "NewFile.txt"
    if not os.path.exists(new_file_path):
        with open(new_file_path, "w") as new_file:
            pass

    number_pattern = re.compile(r"^[0-9]+$")
    firstname_lastname_pattern = re.compile(r"^([A-Z]{1})[a-z]+([A-Z]{1})[a-z]+$")
    date_of_birth_pattern = re.compile(r"^(0[1-9]|1[0-2])[0-9]/[01-12]\d{1,2}/\d{4}$")
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$")
    mobile_number_pattern = re.compile(r"^\+[0-9]{10}$")
    iban_pattern = re.compile(r"^KZ\d{20}$")

    insert_text_into_file(new_file_path, "Number: 1", number_pattern)
    insert_text_into_file(new_file_path, "Firstname Lastname: John Smith", firstname_lastname_pattern)
    insert_text_into_file(new_file_path, "Date of birth: 11/02/1990", date_of_birth_pattern)
    insert_text_into_file(new_file_path, "Email: john@gmail.com", email_pattern)
    insert_text_into_file(new_file_path, "Mobile number: +7(701)777-77-77", mobile_number_pattern)
    insert_text_into_file(new_file_path, "IBAN: KZ12345678901234567890", iban_pattern)

    # Close the file
    with open(new_file_path, "r") as file:
        file_contents = file.read()

    print(file_contents)
