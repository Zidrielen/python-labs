import os

import pandas as pd
import cv2

def append_abs_path(abs_path_to_files: list,
                    list_files: list, dir: list) -> None:
    '''Adding the full path to a file to the list'''
    for files in list_files:
        path = os.path.join(dir, files)
        abs_path_to_files.append(path)


def part_1() -> pd.core.frame.DataFrame:
    '''Creating a DataFrame with column names'''
    project_path = os.path.abspath("")
    cat_dir = os.path.join(project_path, "dataset", "cat")
    dog_dir = os.path.join(project_path, "dataset", "dog")

    files_cat = os.listdir(cat_dir)
    files_dog = os.listdir(dog_dir)
    class_ = list(["cat"] * len(files_cat)) + list(["dog"] * len(files_dog))

    abs_path_to_files = []
    append_abs_path(abs_path_to_files, files_cat, cat_dir)
    append_abs_path(abs_path_to_files, files_dog, dog_dir)

    return pd.DataFrame({
        "class": class_,
        "abspath": abs_path_to_files
    })


def part_2(my_series: pd.core.frame.DataFrame) -> None:
    '''Create a column with numeric labels'''
    i = 0

    for class_ in my_series["class"]:
        if class_ == "cat":
            my_series.loc[[i], ["num_label"]] = "0"
        else:
            my_series.loc[[i], ["num_label"]] = "1"
        i += 1


def part_3(my_series: pd.core.frame.DataFrame) -> None:
    '''Creating columns with image options'''
    cat_dir = os.path.join( "dataset", "cat")
    dog_dir = os.path.join( "dataset", "dog")

    files_cat = os.listdir(cat_dir)
    files_dog = os.listdir(dog_dir)

    characters_img = []

    for file in files_cat:
        image = cv2.imread(os.path.join(cat_dir, file))
        characters_img.append(image.shape)
    
    for file in files_dog:
        image = cv2.imread(os.path.join(dog_dir, file))
        characters_img.append(image.shape)
    
    i = 0

    for data in characters_img:
        my_series.loc[[i], "width"] = str(data[0])
        my_series.loc[[i], "height"] = str(data[1])
        my_series.loc[[i], "depth"] = str(data[2])
        i += 1
  

def main() -> None:

    my_series = part_1()
    part_2(my_series)
    part_3(my_series)



