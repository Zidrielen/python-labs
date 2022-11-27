import os
from typing import Type

import pandas as pd
import cv2


def append_abs_path(abs_path_to_files: list,
                    list_files: list, dir: list) -> None:
    '''Adding the full path to a file to the list'''
    for files in list_files:
        path = os.path.join(dir, files)
        abs_path_to_files.append(path)


def part_1() -> pd.core.series.Series:
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


def part_2(my_series: pd.core.series.Series) -> None:
    '''Create a column with numeric labels'''
    i = 0

    for class_ in my_series["class"]:
        if class_ == "cat":
            my_series.loc[[i], ["label"]] = 0
        else:
            my_series.loc[[i], ["label"]] = 1
        i += 1


def part_3(my_series: pd.core.series.Series) -> None:
    '''Creating columns with image options'''
    cat_dir = os.path.join( "dataset", "cat")
    dog_dir = os.path.join( "dataset", "dog")

    files_cat = os.listdir(cat_dir)
    files_dog = os.listdir(dog_dir)

    i = 0

    for file in files_cat:
        image = cv2.imread(os.path.join(cat_dir, file))
        data = image.shape
        my_series.loc[[i], "height"] = data[0]
        my_series.loc[[i], "width"] = data[1]
        my_series.loc[[i], "depth"] = data[2]
        i += 1
    
    for file in files_dog:
        image = cv2.imread(os.path.join(dog_dir, file))
        data = image.shape
        my_series.loc[[i], "height"] = data[0]
        my_series.loc[[i], "width"] = data[1]
        my_series.loc[[i], "depth"] = data[2]
        i += 1


def part_4(my_series: pd.core.series.Series) -> None:
    '''Generates statistical information(Data is balanced)'''
    print(my_series.describe())
    

def part_5(my_series: pd.core.series.Series,
           label: int) -> pd.core.series.Series:
    '''Returns a DataFrame with the given label'''
    return my_series[my_series["label"] == label]


def part_6(my_series: pd.core.series.Series, label: int,
           h: int, w: int) -> pd.core.series.Series:
    '''Returns a DataFrame with the given label and appropriate dimensions'''
    tmp_1 = my_series[my_series["label"] == label]
    tmp_2 = tmp_1[tmp_1["height"] <= h]
    return tmp_2[tmp_2["width"] <= w]





def main() -> None:
    '''Start'''
    my_series = part_1()
    part_2(my_series)
    part_3(my_series)
    print(part_4(my_series))
    #series_label = part_5(my_series, 1)
    #print(series_label)
    #print(part_6(my_series, 0, 320, 400))


