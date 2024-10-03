import os

## Open the txt file and read it by line
with open('SENTENCE_NAME_DEV.txt', 'r') as f:
    file_list = [line.strip() for line in f.readlines()]

## Remove the newline and traverse the list of files
for index, file_name in enumerate(file_list):
    file_name = file_name.strip()
    mp4_name = str(file_name) + '.mp4'

    # Rename mp4 file
    if os.path.isfile(mp4_name):
        new_name = str(index + 1).zfill(6) + '.mp4'
        os.rename(mp4_name, new_name)

