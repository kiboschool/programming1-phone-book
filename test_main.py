import unittest
from main import *

class Test(unittest.TestCase):
    def test_add_contact(self):
        phonebook = {}
        name = "Ope"
        number = "+234 555 666 7777"
        result = add_contact(phonebook, name, number)
        self.assertEqual(result, f"{name} added")
        self.assertEqual(phonebook[name], number)
        self.assertEqual(len(phonebook), 1)

    def test_add_contact_already_present(self):
        phonebook = {"Ope": "+234 555 666 7777"}
        name = "Ope"
        number = "+234 555 666 7777"
        result = add_contact(phonebook, name, number)
        self.assertEqual(result, f"{name} is already in phonebook")

    def test_find_contact(self):
        phonebook = {"Ope": "+234 555 666 7777"}
        phonebook_copy = {"Ope": "+234 555 666 7777"}
        name = "Ope"
        result = find_contact(phonebook, name)
        self.assertEqual(result, "+234 555 666 7777")
        # no modifications
        self.assertEqual(phonebook, phonebook_copy)

    def test_find_contact_missing(self):
        phonebook = {"Ope": "+234 555 666 7777"}
        phonebook_copy = {"Ope": "+234 555 666 7777"}
        name = "Oyin"
        result = find_contact(phonebook, name)
        self.assertEqual(result, "Oyin not found")
        # no modifications
        self.assertEqual(phonebook, phonebook_copy)

    def test_update_contact(self):
        phonebook = {"Ope": "+234 555 555 5555"}
        name = "Ope"
        number = "+233 444 555 6666"
        result = update_contact(phonebook, name, number)
        self.assertEqual(result, f"{name} updated")
        self.assertEqual(phonebook[name], number)
        self.assertEqual(len(phonebook), 1)
    
    def test_update_contact_missing(self):
        phonebook = {"Ope": "+234 555 555 5555"}
        name = "Oyin"
        number = "+233 444 555 6666"
        result = update_contact(phonebook, name, number)
        self.assertEqual(result, f"{name} not found")
        self.assertEqual(len(phonebook), 1)

    def test_delete_contact(self):
        phonebook = {"Ope": "+234 555 555 5555"}
        name = "Ope"
        result = delete_contact(phonebook, name)
        self.assertEqual(result, f"{name} deleted")
        self.assertEqual(len(phonebook), 0)
    
    def test_delete_contact_missing(self):
        phonebook = {"Ope": "+234 555 555 5555"}
        name = "Oyin"
        result = delete_contact(phonebook, name)
        self.assertEqual(result, f"{name} not found")
        self.assertEqual(len(phonebook), 1)

    def test_list_contacts(self):
        phonebook = {
                "Ope": "+234 555 555 5555",
                "Oyin":"+233 444 555 6666"
                }
        result = list_contacts(phonebook)
        self.assertEqual(result, "Ope: +234 555 555 5555\nOyin: +233 444 555 6666\n")

if __name__ == '__main__':
    unittest.main()
