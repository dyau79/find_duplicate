import os
import hashlib
from pathlib import Path

def find_duplicates(folder_path):
    # Initialize a dictionary to store file hashes and their corresponding paths
    duplicates = {}

    # Traverse the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            # Construct the full file path
            file_path = os.path.join(root, file_name)

            # Calculate the hash of the file
            file_hash = hash_file(file_path)

            # Add or append the file path to the duplicates dictionary
            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]

    # Filter out unique files (lists with only one element)
    return [paths for paths in duplicates.values() if len(paths) > 1]

def hash_file(file_path):
    # Calculate the MD5 hash of the file
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        # Read the file in chunks and update the hash
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            hasher.update(chunk)

    return hasher.hexdigest()

def main():
    folder_path = Path('path/to/directory')

    # Find duplicates in the specified folder
    duplicate_files = find_duplicates(folder_path)

    if duplicate_files:
        print("Duplicate files found:")
        for duplicate in duplicate_files:
            print("\n".join(duplicate))
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    main()