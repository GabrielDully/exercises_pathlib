'''
File Renaming:
Create a Python script that renames all text files (with the extension .txt) in a given directory by adding a prefix "new_" to their filenames. Use pathlib for directory traversal and file renaming.
'''


from pathlib import Path

def rename_txt_files(directory_str):

    directory_path = Path(directory_str)

    if not directory_path.exists():
        return False 

    prefix = '/new_'
    suffix = '.txt'
    i = 1
    for item in directory_path.iterdir():

        item_path = Path(item)
        if item_path.suffix == '.txt':
            
            item_path.rename(directory_str + prefix + str(i) + suffix)
            i += 1
