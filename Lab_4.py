import os
from typing import Type
from random import randint

import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt


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
    relpaths = []
    for i in range(0, my_series["abspath"].count()):
        abspath = my_series.iloc[i, 1]
        relpaths.append(abspath[-20:])
    
    j = 0
    for path in relpaths:
        image = cv2.imread(path)
        data = image.shape
        my_series.loc[[j], "height"] = data[0]
        my_series.loc[[j], "width"] = data[1]
        my_series.loc[[j], "depth"] = data[2]
        j += 1


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


def part_7(my_series: pd.core.series.Series, label: int) -> None:
    '''Creates a column with the number of pixels 
       and outputs the minimum, maximum, and median pixels'''
    my_series["pixels"] = (my_series["height"] *
                           my_series["width"]  *
                           my_series["depth"])
    
    print("The maximum number of pixels is ", my_series["pixels"].max())
    print("The minimum number of pixels is", my_series["pixels"].min())
    print("The average number of pixels is", my_series["pixels"].mean())


def part_8(my_series: pd.core.series.Series, label: int) -> np.ndarray:
    
    label_series = my_series[my_series["label"] == label]
    rand_num = randint(0, label_series["abspath"].count())
    abspath = my_series.iloc[rand_num, 1]
    relpath = abspath[-20:]

    image = cv2.imread(relpath)

    histr_1 = cv2.calcHist([image], [0], None, [256], [0,256])
    histr_2 = cv2.calcHist([image], [1], None, [256], [0,256])
    histr_3 = cv2.calcHist([image], [2], None, [256], [0,256])
    
    return histr_1, histr_2, histr_3


def part_9(histr_1: np.ndarray, histr_2: np.ndarray,
           histr_3: np.ndarray) -> np.ndarray:
    
    col = ('b','g','r')
    plt.plot(histr_1, color=col[0])
    plt.plot(histr_2, color=col[1])
    plt.plot(histr_3, color=col[2])
    plt.xlabel("value")
    plt.ylabel("count")
    plt.title("histogram")
    plt.xlim([0,256])
    plt.show()


def main() -> None:
    '''Start'''
    my_series = part_1()
    part_2(my_series)
    part_3(my_series)
    print(my_series)
    #print(part_4(my_series))
    #series_label = part_5(my_series, 1)
    #print(series_label)
    #print(part_6(my_series, 0, 320, 400))
    #part_7(my_series, 0)
    #histr_1, histr_2, histr_3 = part_8(my_series, 0)
    #part_9(histr_1, histr_2, histr_3)
