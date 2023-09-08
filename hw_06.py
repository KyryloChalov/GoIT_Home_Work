import sys
import shutil
from pathlib import Path


CATEGORIES = {
           "Archives": [".zip", ".gz", ".tar"],
              "Audio": [".mp3", ".wav", ".flac", ".wma", ".ogg"],
              "Video": [".avi", ".mp4", ".mov", ".mkv"],
             "Images": [".jpeg", ".png", ".jpg", ".svg", ".gif"],
          "Documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
              "Other": []
              }

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "jo", "zh", "z", "y", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "'", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

def prepare_trans() -> None:
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return

def normalize_name(file_name:str) -> str: 
    file_name_split = file_name.split(".")
    
    result = ""
    name = file_name_split[0]
    for n in range(len(file_name_split) - 2):
        name += "_" + file_name_split[n+1]
    for i in range(len(name)):
        if name[i] == " ":
            result += " "
        elif "0" <= name[i] <= "9":         # numbers
            result += name[i]
        elif "a" <= name[i] <= "z":         # a..z
            result += name[i]
        elif "A" <= name[i] <= "Z":         # A..Z
            result += name[i]
        elif ord(name[i]) in TRANS:         # cyrylic
            result += TRANS[ord(name[i])]
        else:
            result += "_"
    return result

def normalize_extension(file_name:str) -> str:
    file_name_split = file_name.split(".")
    ext = "."
    if len(file_name_split) > 1: # file extension != ""
        ext += file_name_split[-1]
    return ext

def normalize(file_name:str) -> str:
    return normalize_name(file_name) + normalize_extension(file_name)


def del_empty_tree(path:Path) -> None:
    
    for element in path.glob("**/*"):
        if element.is_dir():           
            if str(element).split("\\")[-1] not in CATEGORIES:
                shutil.rmtree(element)                
    

def get_categories(file:Path) -> str:
    
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def move_file(file:Path, category:str, root_dir:Path) -> None:
    
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    
    new_path = target_dir.joinpath(normalize(file.name))
    
    file.replace(new_path)          # replase if exist
    
    # if not new_path.exists():     # NOT replase if exist
        # file.replace(new_path)

                
def archive_unpack(root_dir:Path) -> None:
    
    category = list(CATEGORIES.keys())[0]  
                # "Archives" must be first in the list (dict CATEGORIES) !!!
    path = Path(str(root_dir) + "\\" + category)
    if path.exists():
        for element in path.glob("**/*"):
            if element.is_file() and normalize_extension(str(element)) in list(CATEGORIES.values())[0]:            
                shutil.unpack_archive(element, (str(path) + "\\" + normalize_name(str(element.name))))
    

def sort_folder(path:Path) -> None:
    
     for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)


def list_files(path:Path, echo_list=True) -> None:
    
    file_list = str(path) + "\\" + "_file_list_.txt"
    with open(file_list, 'w') as file_out:
        file_out.write("        List Of Files: ")
        if echo_list: print("        List Of Files: ")
    
    with open(file_list, 'a') as file_out:
        for element in path.glob("**/*"):
            if str(element).split("\\")[-1] != file_list.split("\\")[-1]:
                if echo_list: print(element)
                file_out.write("\n" + str(element))
        

def list_files_category(path:Path) -> None:
    for element in path.glob("**/*"):
        if element.is_dir():
            category = str(element).split("\\")[-1]
            list_files(Path(str(path) + "\\" + category), False)
            
            
def prepare_folder() -> None:                       # це для отладки 
    TEST_FOLDER = "D:\\000"                         # особисто моєї отладки :)
    SOURSE_FOLDER = "D:\\000_Original"
    shutil.rmtree(TEST_FOLDER, ignore_errors=True)
    p = input("press any key >>> ")  # пауза
    shutil.copytree(SOURSE_FOLDER, TEST_FOLDER)
    

def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
    
    if not path.exists():
        return "Folder dos not exists"
    
    # prepare_folder()        # прибрати - це для отладки
    
    prepare_trans()         # for transliteration
    sort_folder(path)       
    del_empty_tree(path)
    list_files(path)
    list_files_category(path)
    archive_unpack(path)    # щоб файли з архівів теж були у списку, перенести цю строку вище
    
    return "\n*** Completed Successfully ***\n"

 
if __name__ == '__main__':
    print(main())
