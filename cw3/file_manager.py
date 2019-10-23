# file_manager.py
# zadanie 8

class FileManager():
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def read_file(self):
        self.file = open(self.file_name, 'r', encoding='utf-8')
        data = self.file.read()
        self.file.close()
        return data

    def update_file(self, text_data):
        self.file = open(self.file_name, 'w', encoding='utf-8')
        data = self.file.write(text_data)
        self.file.close()
