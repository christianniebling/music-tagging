import os

# Options
REMOVE_STRING = "Twenty  One  Pilots -"
DIRECTORY_PATH = r"F:\music\library\Twenty One Pilots\Regional At Best"
TARGET_FILE_EXT = ".mp3"
PRINTING = True

# Code

def remove_string_from_filename(file, substring):
    directory_name, base_name = os.path.split(file)
    new_base_name = base_name.replace(substring, '')
    new_file_name = os.path.join(directory_name, new_base_name)
    os.rename(file, new_file_name)
    return new_file_name

def main():
    contents = os.listdir(DIRECTORY_PATH)
    for value in contents:
        if value.endswith(TARGET_FILE_EXT):
            old_name = value
            file_path = os.path.join(DIRECTORY_PATH, value)
            new_name = remove_string_from_filename(file_path, REMOVE_STRING)
            if PRINTING:
                print(f'Renamed "{old_name}" to "{new_name}"')


if __name__ == "__main__":
    if os.path.exists(DIRECTORY_PATH):
        main()
    else:
        print("Path not found.")