import os
from shutil import copy2

from Lab_2_1 import create_csv


def create_dir(name_dir: str) -> str:
    path_ = os.path.join("dataset", name_dir)
    if not os.path.isdir(path_):
        os.mkdir(path_)
    return path_


def copy_dataset(path_fol: str, ndp: str, animal: str) -> None:
    path_ =  os.path.join(path_fol, animal)
    names = os.listdir(path_)
    for item in names:
        if ".jpg" in item:
            s = os.path.join(path_, item)
            d = os.path.join(ndp, f'{animal}_{item}')
            copy2(s, d)


    

