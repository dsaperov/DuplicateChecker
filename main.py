import argparse
import os
from collections import defaultdict

parser = argparse.ArgumentParser(epilog='Examples of use:\n'
                                        '- python main.py "C:/Users/My_folder" (to check files of all extensions)\n'
                                        '- python main.py "C:/Users/My_folder" -e txt (to check only files of .txt '
                                        'extension)',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('path',
                    help='path to the folder you need to check for files with duplicate content in. Should be enclosed '
                         'in double quotes (example: "C:/Users/My_folder").')
parser.add_argument('-e', '--extension',
                    help='extension (without a dot) of files to be checked (example: "txt", but not ".txt"). If not '
                         'specified, files of all extensions will be checked.')
args = parser.parse_args()
path = os.path.normpath(args.path)
extension = '.' + os.path.normpath(args.extension) if args.extension else None

filenames_for_hashes = defaultdict(list)
hashes_of_duplicates = set()


def get_hash(filename):
    with open(filename, mode='rb') as file:
        file_content = file.read()
        return hash(file_content)


for name in os.listdir(path):
    f = os.path.join(path, name)
    if os.path.isfile(f):
        if extension and not f.lower().endswith(extension):
            continue
        content_hash = get_hash(f)
        if content_hash in filenames_for_hashes:
            hashes_of_duplicates.add(content_hash)
        filenames_for_hashes[content_hash].append(name)

if hashes_of_duplicates:
    print('Files with duplicate content found:')
    last_hash_number = len(hashes_of_duplicates)
    for i, hash_value in enumerate(hashes_of_duplicates, 1):
        print(*filenames_for_hashes[hash_value], sep='\n')
        if i != last_hash_number:
            print('----------------------')
else:
    print('No files with duplicate content found')
