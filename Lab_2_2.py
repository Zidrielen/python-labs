import os
from shutil import copy2
from pathlib import Path

def create_dir(path_: str) -> str:
    if not os.path.isdir(os.path.join("dataset", path_)):
        os.mkdir(os.path.join("dataset", path_))
    return os.path.join("dataset", path_)


def copy_dataset(class_name: str, ndp: str) -> None:
    for item in os.listdir(os.path.join('dataset', class_name)):
        if ".jpg" in item:
            s = os.path.join(os.path.join('dataset', class_name), item)
            d = os.path.join(ndp, f'{class_name}_{item}')
            copy2(s, d)


def create_csv_for_new_dataset(path_dir: str) -> None:
    path_ = os.path.join("dataset", path_dir)
    names = os.listdir(path_)
    with open(os.path.join(path_, f"{path_dir}_annotation.csv"), 'w') as file_csv:
        for i in names:
            if ".jpg" in i:
                abspath = str(Path(Path.home(), "python-labs", path_, i))
                file_csv.write(abspath+" "+
                               os.path.join(path_, i)+" "+i[0:3]+"\n")
    file_csv.close()


def run_2():
    new_dataset_path = create_dir("new_dataset")
    copy_dataset("cat", new_dataset_path)
    copy_dataset("dog", new_dataset_path)
    create_csv_for_new_dataset("new_dataset")


    

