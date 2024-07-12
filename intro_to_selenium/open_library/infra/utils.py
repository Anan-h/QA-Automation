import string
import random


class Utils:
    """
    This class include helping functions that suitable for every website
    """

    @staticmethod
    def generate_string_of_letters(length):
        """
        This function generates a random string of letters
        :param length:how many times to type a random letter
        :return:random letters as a string
        """
        chars = string.ascii_letters
        return ''.join((random.choice(chars) for i in range(length)))


