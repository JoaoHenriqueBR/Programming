# Rename files (Currently in "dev" version, maybe I will turn this into a project in the future (Like a File Organizer script))

import os

print('{} RENAME MULTIPLE FILES {}'.format('='*10, '='*10))
directory = input('Name of the directory: ')
os.chdir(directory)

c = 0
for f in os.listdir(): # For each file in the directory:
    c += 1 # Counter
    file_name, file_ext = os.path.splitext(f) # split between file name and file extension
    new_name = '{} - EX-{}{}'.format(file_name, c, file_ext) # Choose the new name
    print(f'Renamed to: {new_name}') # Show the new name
    os.rename(f, new_name) # Change the files to the new name
