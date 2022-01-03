from pathlib import Path
# Reference: https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
def create_folder(path: str):
    try:
        Path(path).mkdir(parents = True)
    except FileExistsError:
        print(f'Folder "%s" already exists.' % path)