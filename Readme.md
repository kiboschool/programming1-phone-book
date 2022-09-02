# Phone Book

Dictionaries are great when you want to store information for future lookup. In
this exercise, you'll build a phonebook program that uses a dictionary to store
contacts with their phone numbers.

## Your Task

Write a program that keeps name and phone numbers in a dictionary as key-value pairs.

First, you'll implement functions to operate on the phonebook: add, search,
update, and delete contacts. Those functions will be used from in the text interface of the program to interact with the phonebook.

The program will display a menu that lets the user search for a phone number by name, add a new name and phone number, change an existing phone number, delete a name and phone number, or list all the contacts.

## Starter Code

In `main.py`, the code for the interface has been built out. You need to
implement the 5 functions to manage the phonebook. Each one has the function
signature and a non-functional implementation.

### `add_contact`

This function takes in the phonebook and a name and number. It should add the
name and number to the phonebook and return a message saying the contact was
added.

If the name is already in the phonebook, it should return amessage saying so,
like "Ope is already in the phonebook".

### `find_contact`

This function takes in the phonebook and a name, and should return the number 
for a contact, if it is in the phonebook.

If the name is not in the phonebook, it should return a message saying the
contact wasn't found, like "Funminiyi not found"

### `update_contact`

This function takes in the phonebook, a name, and a new number. If the contact
is in the phonebook, it should update the number and returna message saying the
contact was updated.

If the contact was not in the phonebook, it should return a message saying the
contact was not found.

### `delete_contact` 

This function takes in the phonebook and a name. If the name was in the
phonebook, it should delete it and return a message saying it was deleted. 

If the name was not in the phonebook, it should return a message saying that the 
contact wasn't found.

### `list_contacts`

This function takes in the phonebook, and _returns_ (not prints!) a string with
all of the names and numbers in the phonebook.

## Testing

As you implement each function, you can run the automated tests to check that
the function is working correctly. 

After you've implemented all of the functions, you should run the program
interactively to check that your solution works.

## Expected Results

Here's a sample run. All but the first menu and "Press Enter to Continue" 
message have been omitted, to save space. 

```txt
$ python main.py

Menu
1. Add a contact
2. Search a contact
3. Change a contact
4. Delete a contact
5. List all contacts
6. Exit
Enter your choice: 1
Enter name: Ope
Enter a phone number: +234 555 666 7777
Ope added
Press Enter to continue.

Enter your choice: 2
Enter name: Ope
+234 555 666 7777

Enter your choice: 1
Enter name: Oyin
Enter a phone number: +234 555 666 7777
Oyin added

Enter your choice: 5
Ope: +234 555 666 7777
Oyin: +234 555 666 7777


Enter your choice: 3
Enter name: Oyin
Enter new phone number: +234 555 555 5555
Oyin updated

Enter your choice: 5
Ope: +234 555 666 7777
Oyin: +234 555 555 5555


Enter your choice: 4
Enter name: Ope
Ope deleted

Enter your choice: 5
Oyin: +234 555 555 5555


Enter your choice: 4
Enter name: Ope
Ope not found

Enter your choice: 3
Enter name: Ope
Enter new phone number: +234 555 555 5555
Ope not found

Enter your choice: 6
Thank you!
```

## Bonus Task

Right now, the phonebook only exists while the program is running. Instead of
losing all the contact information when the program exits, save the contacts to
a file when the program exits. Then, when the program starts, load the file.
