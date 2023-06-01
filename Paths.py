import os

master_path = "/Users/peterhicks/Pictures/UI_Compare/Master/"
test_path = "/Users/peterhicks/Pictures/UI_Compare/Test/"
result_path = "/Users/peterhicks/Pictures/UI_Compare/Result/"
screen_paths = "/Users/peterhicks/Pictures/UI_Compare/Master/iPhone_14/"


def get_files_in_directory(directory_path):
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path is not a directory: {directory_path}")

    # Get all files in directory, excluding the .DS_Store file
    files = [f for f in os.listdir(directory_path) if
             os.path.isfile(os.path.join(directory_path, f)) and f != '.DS_Store']

    # Define a custom sorting function.
    # We assume that the filename starts with a number and ends with .png (or another extension)
    def sort_key(filename):
        # split the filename by dot, take the first part and convert it to an integer
        return int(filename.split(".")[0])

    # Sort the files using the custom sorting function
    files.sort(key=sort_key)

    return files


def get_subdirectories_in_directory(directory_path):
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        raise ValueError(f"The provided path is not a directory: {directory_path}")

    # Get all subdirectories in directory, excluding any that begin with a dot
    dirs = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d)) and not d.startswith('.')]

    # Sort the directories (assuming they have numerical names)
    dirs.sort(key=lambda d: int(d.split(".")[0]) if d.split(".")[0].isdigit() else float('inf'))

    return dirs


screen_type = get_subdirectories_in_directory(screen_paths)