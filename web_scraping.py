from os import mkdir, remove, listdir, rename, path
from time import sleep
from imghdr import what

import requests
from bs4 import BeautifulSoup
from cv2 import imread, Mat
import np


LINK_YANDEX="https://yandex.ru/images/search?text="
LINK_PART_2="&p="
DOG="dog"
CAT="cat"


def save_html(link):
    return requests.get(link).text


def load_image(link):
    return requests.get(link, stream=True).content


def save_image(response, animal, n):
    soup = BeautifulSoup(response, "lxml")
    all_link_tag_img = soup.find_all("img", class_="serp-item__thumb justifier__thumb")
    for link_tag_img in all_link_tag_img:
        sleep(5)
        image = load_image("http:" + link_tag_img.get("src"))
        name = str(n).zfill(4)
        path = f"dataset\{animal}\{name}.jpg"
        file = open(path, "wb")
        file.write(image)
        file.close()
        n += 1
        

def push_image(animal):
    for i in range(0, 40):
        n = 30 * i
        sleep(30)
        response = save_html(LINK_YANDEX + animal + LINK_PART_2 + str(i))
        save_image(response, animal, n)


def make_dir():
    '''Make directories for images'''
    if not path.isdir("dataset"):
        mkdir("dataset")
    if not path.isdir("dataset\cat"):
        mkdir("dataset\cat")
    if not path.isdir("dataset\dog"):
        mkdir("dataset\dog")


def cheking_format(path_to_folder: str):
    images = listdir(path_to_folder)
    for image in images:
        path_to_image = f"{path_to_folder}/{image}"
        if(what(path_to_image) != "jpeg"):
            remove(path_to_image)


def rename_image(path_to_folder: str) -> None:
    '''Changing the name of images'''
    images = listdir(path_to_folder)
    for i, image in enumerate(images):
        before = f"{path_to_folder}/{image}"
        after = f"{path_to_folder}/{str(i).zfill(4)}.jpg"
        rename(before, after)


def delete_dublicate(path_to_folder: str) -> None:
    image = listdir(path_to_folder)
    num_images = len(image) - 1
    i, j = 0, 0

    img_data = []
    for img in image:
        img_data.append(imread(f"{path_to_folder}/{img}"))

    while i < num_images:
        index_array = []
        j = i + 1

        while j <= num_images:
            if np.all(compare_images(img_data[i], img_data[j])):
                remove(f"{path_to_folder}/{image[j]}")
                print(image[i], "+", image[j])
                index_array.append(j)
            j += 1

        for index in index_array:
            del img_data[index]
            del image[index]
        num_images = len(image) - 1
        print(f"Compare {image[i]} complete")
        i += 1


def compare_images(img_1: Mat, img_2: Mat) -> bool:
    return img_1 == img_2


def main():
    PATH_TO_DOG = "dataset/dog"
    PATH_TO_CAT = "dataset/cat"
    
    make_dir()

    push_image(CAT)
    push_image(DOG)

    cheking_format(PATH_TO_CAT)
    cheking_format(PATH_TO_DOG)

    delete_dublicate(PATH_TO_CAT)
    delete_dublicate(PATH_TO_DOG)

    rename_image(PATH_TO_CAT)
    rename_image(PATH_TO_DOG)