# Rename files

import os

print('{} RENAME MULTIPLE FILES {}'.format('='*10, '='*10))
directory = input('Name of the directory: ')
os.chdir(directory)

c = 0
for f in os.listdir():
    c += 1
    file_name, file_ext = os.path.splitext(f)
    new_name = '{} - EX-{}{}'.format(file_name, c, file_ext)
    os.rename(f, new_name)
