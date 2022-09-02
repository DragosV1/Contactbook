from contact_book import ContactBook


def store_contact():
    """It will generate an txt file"""

    contact = ContactBook(
        name=input("Enter the name of the contact: "),
        phone_number=input("Enter the phone number: "),
        address=input("Enter the address: "),
        email=input("Enter email: ")
    )

    print(contact.check_phone_number())
    print(contact.check_email())
    print(contact.describe_contact(), "\n")

    with open("./contacts.txt", "a") as f:
        f.writelines((contact.describe_contact(), "\n"))

def search_contact():
    with open("contacts.txt", "r") as f:
        search = input("\nSearch contact: ")
        for i in f:
            if search in i:
                print(i)

def delete_contact():
    delete_value = input("\nDelete contact: ")
    with open("contacts.txt", "r") as f:
        lines = f.readlines()
    with open("contacts.txt", "w") as fw:
        for line in lines:
            if delete_value not in line:
                fw.write(line)

def show_contact_book():
    with open("contacts.txt", "r") as f:
        print(f.read().replace("\n", "| "))

while True:
    user_input = input("\nAdd contact (A)\nSearch contact (S)\nDelete contact (D)\nSee all contacts(R)\nQuit (Q)\nType: ").upper()
    if user_input == "A":
        store_contact()
    elif user_input == "S":
        search_contact()
    elif user_input == "D":
        delete_contact()
    elif user_input == "R":
        show_contact_book()
    elif user_input == "Q":
        print("\nYou have closed the program!")
        quit()
    else:
        print("\nYou entered the wrong letter!")
        quit()