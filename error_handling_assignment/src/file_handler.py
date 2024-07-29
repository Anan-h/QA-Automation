import contextlib

from error_handling_assignment.src.file_processing_error import FileProcessingError


class FileHandler(contextlib.ContextDecorator):
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
            return self.file
        except Exception as e:
            raise FileProcessingError(f"Error: {str(e)}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"File {self.file_path} has been closed.")
        if exc_type:
            raise FileProcessingError(f"Error: {str(exc_val)}")