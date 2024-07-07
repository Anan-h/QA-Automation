import string
import random


class Utils_G:
    @staticmethod
    def generate_string(length):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join((random.choice(chars) for i in range(length)))

    @staticmethod
    def generate_string_of_numbers(length):
        return ''.join((random.choice(string.digits) for i in range(length)))
