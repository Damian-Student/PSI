import cw3.file_manager

fm = cw3.file_manager.FileManager("some_file.txt")
print(fm.read_file())
fm.update_file("nie smieszne")
print(fm.read_file())