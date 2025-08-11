class FileOperations:
    def __init__(self):
        self.file_name = ""

    def create_file(self):
        self.file_name = input("Enter the file name (e.g. file.txt): ")
        with open(self.file_name, "w") as f:
            print(f"File '{self.file_name}' created successfully.")

    def write_to_file(self):
        content = input("Enter content to write to the file:\n")
        with open(self.file_name, "w") as f:
            f.write(content)
        print(f"Content written to '{self.file_name}' successfully.")

    def read_file(self):
        try:
            with open(self.file_name, "r") as f:
                content = f.read()
                print("File content:\n", content)
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")

    def append_to_file(self):
        content = input("Enter content to append to the file:\n")
        with open(self.file_name, "a") as f:
            f.write(content + "\n")
        print(f"Content appended to '{self.file_name}' successfully.")
