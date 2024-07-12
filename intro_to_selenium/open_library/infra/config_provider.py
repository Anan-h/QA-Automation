import json


class ConfigProvider:
    """
    This class is to provide data from outer file
    """

    @staticmethod
    def load_from_file(filename):
        """
        This function return a read only file that include data
        :param filename:the file name and location
        :return:
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")