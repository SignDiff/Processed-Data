import os

##Open the txt file and read it by line
with open('SENTENCE_NAME_DEV.txt', 'r') as f:
    file_list = [line.strip() for line in f.readlines()]

##Remove the newline and traverse the list of files
for index, file_name in enumerate(file_list):
    file_name = file_name.strip()

    # Rename folder
    if os.path.isdir(file_name):
        new_name = str(index + 1).zfill(6)
        os.rename(file_name, new_name)

