import os
from shutil import copyfile
from random import sample

def create_dir(name_dir: str) -> str:
    '''Create a folder'''
    path_ = os.path.join("dataset", name_dir)
    if not os.path.isdir(path_):
        os.mkdir(path_)
    return path_


def copy_dataset(path_fol: str, ndp: str, animal: str) -> None:
    '''Copying the dataset in accordance with item 2 of laboratory №2'''
    path_ =  os.path.join(path_fol, animal)
    names = os.listdir(path_)
    for item in names:
        if ".jpg" in item:
            old_location = os.path.join(path_, item)
            new_location = os.path.join(ndp, f'{animal}_{item}')
            copyfile(old_location, new_location)


def randNames_create_csv(ndp: str) -> None:
    '''Copying the dataset in accordance with item 3 of laboratory №2'''
    names_list = os.listdir(ndp)
    rand_num_array = sample(range(0, 10001), len(names_list))
    n = ndp.rfind("\\")
    name_csv = "annotation.csv"

    with open(os.path.join(ndp, name_csv), 'w') as file_csv:
        for index, file in enumerate(names_list):
            if ".jpg" in file:
                old_name = os.path.join(ndp, file)
                new_name = os.path.join(ndp, f'{rand_num_array[index]}.jpg')
                os.rename(old_name, new_name)
                line = new_name + " " + f"{rand_num_array[index]}.jpg" + " " + file[0:3] + "\n"
                file_csv.write(line)