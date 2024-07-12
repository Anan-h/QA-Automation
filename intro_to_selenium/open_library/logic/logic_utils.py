import string
import random


class LogicUtils:
    """
    this is a class functions especially for the open library website
    """

    @staticmethod
    def generate_random_email_address():
        """
        This function generates a random gmail address
        :return:random gmail address
        """
        end = "@gmail.com"
        letters = string.ascii_letters
        start = ''.join((random.choice(letters)) for i in range(6))
        return start + end

    @staticmethod
    def generate_password():
        """
        This function generates a random password
        :return: string of digits
        """
        password = string.ascii_letters + string.digits
        return ''.join((random.choice(password)) for i in range(10))
