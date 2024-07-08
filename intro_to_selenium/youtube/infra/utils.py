import string
import random


class Utils:
    @staticmethod
    def generate_string_of_letters(length):
        chars = string.ascii_letters
        return ''.join((random.choice(chars) for i in range(length)))

    @staticmethod
    def generate_string_of_numbers(length):
        return ''.join((random.choice(string.digits) for i in range(length)))
