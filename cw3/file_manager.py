# file_manager.py
# zadanie 8

class FileManager():
    def __init__(self, file_name):
        self.file_name = open(file_name)

    def read_file(self):
        data = self.file_name.read()
        return data

    def update_file(self, text_data):
        self.file_name.write(text_data)

    def __del__ (self):
        self.file_name.close()