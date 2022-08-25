"""This is a simple application that stores in a file, searches and deletes contacts from that file"""

import re
import sys

class ContactBook:


    def __init__(self, name, phone_number, address):
        """The ContactBook constructor that takes in the contact name, phone number and address"""
        self.name = name
        self.phone_number = phone_number
        self.address = address

    def check_phone_number(self):
        phone_number_regex = re.compile(r"0\d{3} \d{3} \d{3}|0\d{3} \d{2} \d{2} \d{2}")
        match = phone_number_regex.search(self.phone_number)
        if match is not None:
            return f"Correct phone number: {self.phone_number}"
        else:
            print(f"{ValueError}: Incorrect phone number: {self.phone_number}")
            sys.exit(1)

    def describe_contact(self):
        result = f"Name: {self.name}, Phone number: {self.phone_number}, Address: {self.address} "
        return result