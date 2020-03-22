# d_path = 'data_source.txt'
# d_r_path = 'data_result.txt'
# # with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
# with open(d_path, 'r') as reader:
#     with open(d_r_path, 'w') as writer:
#         data_source = reader.readlines()
#         writer.writelines(reversed(data_source))
#
import os

# os.environ['YOUR_ENV'] = 'SOME_VARIABLE'
# your_env = os.environ.get('YOUR_ENV')
# pass
#
# dirs = list(os.scandir())
#
# import os
#
# with os.scandir('csv_examples/') as entries:
#     for entry in entries:
#         print(entry.name)
#
# entries = os.listdir('csv_examples/')
#
# from pathlib import Path
#
# entries = Path('csv_examples/')
# for entry in entries.iterdir():
#     print(entry.name)

# List all files in a directory using os.listdir
# basepath = './'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath, entry)):
#         print(entry)
#
# basepath = './'
# with os.scandir(basepath) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)
#
# import os
# with os.scandir('./') as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)
#
#
# from pathlib import Path
# current_dir = Path()
# for path in current_dir.iterdir():
#     info = path.stat()
#     print(info.st_mtime)
#
# from datetime import datetime
# from os import scandir
#
#
# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date
#
#
# def get_files():
#     dir_entries = scandir('./')
#     for entry in dir_entries:
#         if entry.is_file():
#             info = entry.stat()
#             print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')
#
# get_files()

# os.mkdir('example_directory/')

# p = Path('example_directory_2/')
# p.mkdir()

# os.makedirs('2018/10/05', exist_ok=True)
# os.unlink('2018/10/05')
# import shutil
import pickle

pass
