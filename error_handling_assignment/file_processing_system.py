from error_handling_assignment.src.file_processor import FileProcessor


class FileProcessingSystem:
    def __init__(self):
        self.processor = FileProcessor()

    def process(self):
        file_path = input("Enter the file path: ")
        operation = input("Enter the operation (read/write): ")

        if operation.lower() == "write":
            content = input("Enter the content to write to the file: ")
            self.processor.write_file(file_path, content)
        elif operation.lower() == "read":
            content = self.processor.read_file(file_path)
            if content:
                print(content)
        else:
            print("Invalid operation. Please enter 'read' or 'write'.")


if __name__ == "__main__":
    system = FileProcessingSystem()
    system.process()