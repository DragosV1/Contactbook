"""This is a simple application that stores in a file, searches and deletes contacts from that file"""

import re
import sys

class ContactBook:


    def __init__(self, name, phone_number, address, email):
        """The ContactBook constructor that takes in the contact name, phone number, address and email"""
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def check_phone_number(self):
        phone_number_regex = re.compile(r"0\d{3} \d{3} \d{3}|0\d{3} \d{2} \d{2} \d{2}")
        match = phone_number_regex.search(self.phone_number)
        if match is not None:
            return f"Correct phone number: {self.phone_number}"
        else:
            print(f"Incorrect phone number: {self.phone_number}")
            sys.exit(1)

    def check_email(self):
        email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        match = email_regex.search(self.email)
        if match is not None:
            return f"Correct email: {self.email}"
        else:
            print(f"Incorrect email: {self.email}")
            sys.exit(1)

    def describe_contact(self):
        result = f"Name: {self.name}, Phone number: {self.phone_number}, Address: {self.address}, Email: {self.email} "
        return result