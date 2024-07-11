import string
import random


class LogicUtils:

    @staticmethod
    def generate_random_email_address():
        end = "@gmail.com"
        letters = string.ascii_letters
        start = ''.join((random.choice(letters)) for i in range(6))
        return start + end

    @staticmethod
    def generate_password():
        password = string.ascii_letters + string.digits
        return ''.join((random.choice(password)) for i in range(10))
