import os
from shutil import copy2

from Lab_2_1 import create_csv


def create_dir(name_dir: str) -> str:
    path_ = os.path.join("dataset", name_dir)
    if not os.path.isdir(path_):
        os.mkdir(path_)
    return path_


def copy_dataset(class_name: str, ndp: str) -> None:
    path_ =  os.path.join('dataset', class_name)
    names = os.listdir(path_)
    for item in names:
        if ".jpg" in item:
            s = os.path.join(path_, item)
            d = os.path.join(ndp, f'{class_name}_{item}')
            copy2(s, d)


def run_2() -> None:
    new_dataset_path = create_dir("new_dataset")
    copy_dataset("cat", new_dataset_path)
    copy_dataset("dog", new_dataset_path)
    create_csv("new_dataset")


    

