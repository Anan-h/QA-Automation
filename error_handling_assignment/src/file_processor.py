from error_handling_assignment.src.file_handler import FileHandler
from error_handling_assignment.src.file_processing_error import FileProcessingError


class FileProcessor:
    @staticmethod
    def read_from_file(file_path):
        try:
            with FileHandler(file_path, 'r') as file:
                content = file.read()
            return f"File Content: {content}"
        except FileProcessingError as e:
            print(e.message)

    @staticmethod
    def write_in_file(file_path, content):
        try:
            with FileHandler(file_path, 'w') as file:
                file.write(content)
        except FileProcessingError as e:
            print(e.message)
        else:
            print(f"Successfully wrote to the file {file_path}.")

