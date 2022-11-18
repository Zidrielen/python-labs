import os
from pathlib import Path


def class_img(animal: str, names_list: list, n: int) -> str:
    if animal=="cat" or animal=="dog":
        return animal
    else:
        return (names_list[n])[0:3]


def create_csv(file: str, path_fol: str , animal: str) -> None:
    path_ = os.path.join(path_fol, animal)
    names_list = os.listdir(path_)
    n = 0
    
    with open(file, 'a') as file_csv:
        for i in names_list:
            if ".jpg" in i:
                abspath = os.path.join(path_, i)
                class_ = class_img(animal, names_list, n)
                rel_path = os.path.join(animal, i)
                line = abspath+" "+rel_path+" "+class_+"\n"
                file_csv.write(line)
                n += 1