from lib.birthdays import *

def test_birthdays_record():
    birthdays = Birthdays("name", "birthdate")
    birthday_list = BirthdaysList()
    birthday_list.add(birthdays)
    assert birthday_list.birthdays_list[0].name == "name"

