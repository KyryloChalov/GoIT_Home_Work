from clean_folder.functions import (sort_folder, del_empty_tree, list_files, archive_unpack)
from clean_folder.read_argv import (read_path, is_replace)

# \/ наступні три строки зроблено для зручності під час розробки \/
from pathlib import Path
if Path("prepare.py").exists() and Path("D:\\000").exists() and Path("D:\\000_Original").exists():
    import clean_folder.prepare
# ^ не звертайте на них уваги, або закоментуйте ^


def main() -> str:
    
    path = read_path()
    if not path.exists():
        return "Folder dos not exists"
    
    sort_folder(path, is_replace())
    del_empty_tree(path)
    list_files(path)
    archive_unpack(path)  # щоб файли з архівів теж були у списку (нащо?), перенести цю строку вище

    return "\n*** Completed Successfully ***\n"


if __name__ == "__main__":
    print(main())
