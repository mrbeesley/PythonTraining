# this is pseudo code to make a point, it wont run

import os
p = '/path/to/datafile.dat'

def process_file(data_file):
    print('file has been processed')

# process file: LBYL (Look before you leap)
if os.path.exists(p):
    process_file(p)
else:
    print(f'no such file as {p}')


# Process file: EAFP (easier to ask forgiveness than permission)
# this is the more pythonic approach, and is enabled by exceptions
try:
    process_file(p)
except OSError as e:
    print(f'Error: {e}')