import os
from collections import namedtuple

directory = "C:\\Users\\Karina\\Documents\\Elite Staffing"
newest_files = {}
Entry = namedtuple('Entry', ['date', 'file_name'])
duplicate_list = {}


def find_duplicate_files(directory):
    os.chdir(directory)
    for file_name in os.listdir(directory):
        name, ext = os.path.splitext(file_name)
        cached_file = newest_files.get(name)
        this_file_date = os.path.getmtime(file_name)
        if cached_file is None:
            newest_files[name] = Entry(this_file_date, file_name)
        else:
            print(f'${name} is a duplicate --------------')
            duplicate_list[name] = name, ext
            if this_file_date > cached_file.date: #replace with the new one
                newest_files[name] = Entry(this_file_date, file_name)

if __name__ == "__main__":
    for folder_name, sub_folders, filenames in os.walk(directory):
    # Find duplicates in main branch
        # find_duplicate_files(directory)
    # Find duplicates in sub branch
        find_duplicate_files(folder_name)
