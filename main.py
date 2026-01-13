from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    
    pass


class Phone(Field):
  
    def __init__(self, value):
        value_str = str(value)
        if not (value_str.isdigit() and len(value_str) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value_str)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_str = str(phone)
        for i, p in enumerate(self.phones):
            if p.value == phone_str:
                self.phones.pop(i)
                return

    def edit_phone(self, old_phone, new_phone):
        old_str = str(old_phone)
        for i, p in enumerate(self.phones):
            if p.value == old_str:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Old phone number not found.")

    def find_phone(self, phone):
        phone_str = str(phone)
        for p in self.phones:
            if p.value == phone_str:
                return p
        return None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)


if __name__ == "__main__":
    book = AddressBook()

    john = Record("John")
    john.add_phone("1234567890")
    john.add_phone("5555555555")
    book.add_record(john)

    jane = Record("Jane")
    jane.add_phone("9876543210")
    book.add_record(jane)

    for record in book.data.values():
        print(record)

    john.edit_phone("1234567890", "1111222333")
    print(john)

    found = john.find_phone("5555555555")
    print(f"{john.name}: {found}")

    book.delete("Jane")
