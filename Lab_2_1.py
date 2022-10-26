import os
from pathlib import Path


def class_img(name_dir: str, names_list: list, n: int) -> str:
    if name_dir=="cat" or name_dir=="dog":
        return name_dir
    else:
        return (names_list[n])[0:3]


def create_csv(name_dir: str) -> None:
    path_ = os.path.join("dataset", name_dir)
    names_list = os.listdir(path_)
    name_csv = f"{name_dir}_annotation.csv"
    n = 0
    
    with open(os.path.join(path_, name_csv), 'w') as file_csv:
        main_path = os.path.join(str(Path.home()), "python-labs", path_)
        for i in names_list:
            if ".jpg" in i:
                abspath = str(Path(main_path, i))
                class_ = class_img(name_dir, names_list, n)
                line = abspath+" "+os.path.join(path_, i)+" "+class_+"\n"
                file_csv.write(line)
                n += 1


def run_1() -> None:
    create_csv("cat")
    create_csv("dog")