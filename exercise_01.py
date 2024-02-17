'''
File Size Calculation:
Write a Python script that calculates the total size of all files in a given directory (and its subdirectories) using pathlib. Prompt the user to input the directory path and then display the total size in bytes.
'''

from pathlib import Path

def recursive_directory_size_calculator(directory):
    
    size = 0
    for item in directory.iterdir():

        if item.is_dir():
            size += recursive_directory_size_calculator(Path(item))
        else:
            size += Path(item).stat().st_size
    
    return size

    
    


def directory_size_calculator(directory_str = None):
    
    if directory_str == None:
        directory_str = input('Indicate the absolute/relative path of the directory: ')

    directory_path = Path(directory_str)
    if not directory_path.exists():
        return f"Directory '{directory_str}' does not exist in system."
    
    return recursive_directory_size_calculator(directory_path)