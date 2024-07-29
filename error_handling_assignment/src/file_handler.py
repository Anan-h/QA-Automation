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

    def __exit__(self, exception_type, exception_value, exc_tb):
        if self.file:
            self.file.close()
        if exception_type:
            raise FileProcessingError(f"Error: {str(exception_value)}")