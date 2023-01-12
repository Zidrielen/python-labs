from random import randint
from typing import List

import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt


def part_1() -> pd.DataFrame:
    '''Creating a DataFrame with column names'''
    df_start = pd.read_csv("task_1.csv", sep = " ", encoding="windows-1251", header=None)

    return pd.DataFrame({
        "class": df_start.iloc[:, 2],
        "abspath": df_start.iloc[:, 0]
    })


def part_2(my_series: pd.DataFrame) -> None:
    '''Create a column with numeric labels'''
    my_series["label"] = 0

    for i, class_ in enumerate(my_series["class"]):
        if class_ == "dog":
            my_series.iloc[[i], [2]] = 1


def part_3(my_series: pd.DataFrame) -> None:
    '''Creating columns with image options'''
    my_series["height"] = 0
    my_series["width"] = 0
    my_series["depth"] = 0
    my_series["pixels"] = 0

    for i, path in enumerate(my_series["abspath"]):
        data = cv2.imread(path[-20:])
        my_series.iloc[[i], [3]] = data.shape[0]
        my_series.iloc[[i], [4]] = data.shape[1]
        my_series.iloc[[i], [5]] = data.shape[2]
        my_series.iloc[[i], [6]] = data.size


def part_4(my_series: pd.DataFrame) -> None:
    '''Generates statistical information(Data is balanced)'''
    print(my_series.describe())
 

def part_5(my_series: pd.DataFrame, label: int) -> pd.DataFrame:
    '''Returns a DataFrame with the given label'''
    return my_series[my_series["label"] == label]


def part_6(my_series: pd.DataFrame, label: int, h: int, w: int) -> pd.DataFrame:
    '''Returns a DataFrame with the given label and appropriate dimensions'''
    tmp_1 = my_series[my_series["label"] == label]
    tmp_2 = tmp_1[tmp_1["height"] <= h]
    return tmp_2[tmp_2["width"] <= w]


def part_7(my_series: pd.DataFrame, label: int) -> None:
    '''Outputs the minimum, maximum, and median pixels'''
    pixel_my_series = part_5(my_series, label)
    
    print("The maximum number of pixels is ", pixel_my_series["pixels"].max())
    print("The minimum number of pixels is", pixel_my_series["pixels"].min())
    print("The average number of pixels is", pixel_my_series["pixels"].mean())


def part_8(my_series: pd.DataFrame, label: int) -> List[np.ndarray]:
    '''Returns 3 arrays with histograms for each channel'''
    label_series = my_series[my_series["label"] == label]
    rand_num = randint(0, len(label_series["abspath"]))
    abspath = my_series.iloc[rand_num, 1]

    image = cv2.imread(abspath[-20:])

    histr_1 = cv2.calcHist([image], [0], None, [256], [0,256])
    histr_2 = cv2.calcHist([image], [1], None, [256], [0,256])
    histr_3 = cv2.calcHist([image], [2], None, [256], [0,256])
    
    return histr_1, histr_2, histr_3


def part_9(histr_1: np.ndarray, histr_2: np.ndarray,
           histr_3: np.ndarray) -> np.ndarray:
    '''Building histograms'''
    col = ('b','g','r')
    plt.plot(histr_1, color=col[0])
    plt.plot(histr_2, color=col[1])
    plt.plot(histr_3, color=col[2])
    plt.xlabel("value")
    plt.ylabel("count")
    plt.title("histogram")
    plt.xlim([0,256])
    plt.show()