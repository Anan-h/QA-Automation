import json


class ConfigProvider:
    @staticmethod
    def load_from_file(file_name):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"file{f} is not found")
