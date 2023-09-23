from pathlib import Path
import sys

def read_path():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        # return "No path to folder"
        path ="."
        while str(path) == ".":
            path = Path(input("Enter the folder path >>> "))
    return path

def is_replace():
    is_r =""
    yes_answer = ["y", "1", "н"]
    try:
        is_r = sys.argv[2]
    except IndexError:
        while is_r == "":
            is_r = input("Replase files with the same names? (Y/n) >>> ").lower()
    return True if is_r[0] in yes_answer else False
    
