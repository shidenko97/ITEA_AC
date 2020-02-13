# from datetime import datetime
import os
from os import scandir
#
# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date
#
# def get_files():
#     dir_entries = scandir('hw_files/')
#     for entry in dir_entries:
#         if entry.is_file():
#             info = entry.stat()
#             print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
#
# get_files()

def rename_filenames(path='hw_files/'):
    dir_entries = os.scandir(path)
    for entry in dir_entries:
        if entry.is_dir():
            rename_filenames(path=entry.path)
        elif " _ " in entry.name:
            os.rename(entry.path, entry.path.replace(" _ ", '_'))

rename_filenames()