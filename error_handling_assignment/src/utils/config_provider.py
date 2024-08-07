import json


class ConfigProvider:
    @staticmethod
    def load_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(e)
