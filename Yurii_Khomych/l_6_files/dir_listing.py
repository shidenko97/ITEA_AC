import os

with os.scandir() as entries:
    for entry in entries:
        print(entry.name)

entries = os.listdir()


#
from pathlib import Path

#
entries = Path()
for entry in entries.iterdir():
    print(entry.name)
