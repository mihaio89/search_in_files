import os
from datetime import datetime

def search_string_in_files(folder_path, search_string):
    found = False  # Flag to track if the search string is found

    # Convert search_string to lowercase for case-insensitive search
    search_string_lower = search_string.lower()

    # Walk through all files and subdirectories in the specified folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get the creation and modification times of the file
                creation_time = os.path.getctime(file_path)
                modification_time = os.path.getmtime(file_path)

                # Format the timestamps
                creation_time_formatted = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                modification_time_formatted = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        # Convert each line to lowercase and perform case-insensitive search
                        if search_string_lower in line.lower():
                            # Get the relative path from the 'files' directory
                            relative_path = os.path.relpath(file_path, folder_path)
                            print(f'file: {relative_path}')
                            # print(f'Created: {creation_time_formatted}')
                            print(f'modified: {modification_time_formatted}')
                            
                            # Split the line by commas
                            fields = line.strip().split(',')
                            if len(fields) > 2:
                                # Extract fields from index 1 to 2 (inclusive), which is field 2 and 3
                                result_fields = fields[1:3]
                                print(','.join(result_fields))  # Print the extracted fields
                            else:
                                # If there are not enough fields, print the whole line
                                print(f'Line: {line.strip()}')
                            
                            found = True
                            break  # Stop checking further lines after finding the string in the file
            except (UnicodeDecodeError, FileNotFoundError) as e:
                # Log the files that could not be opened and the reason
                print(f"Could not open file: {file_path} - {e}")

    if not found:
        print("Not found")

if __name__ == "__main__":
    # Specify the 'files' directory relative to this script
    folder_path = os.path.join(os.path.dirname(__file__), 'files')
    search_string = input("search for: ")
    search_string_in_files(folder_path, search_string)
