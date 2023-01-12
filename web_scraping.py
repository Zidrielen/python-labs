from os import mkdir, remove, listdir, rename, path
from urllib.parse import unquote
from time import sleep
from imghdr import what

import requests
from bs4 import BeautifulSoup
from cv2 import imread
import np
import re


def make_dir():
    '''Make directories for images'''
    if not path.isdir("new_dataset"):
        mkdir("new_dataset")
    if not path.isdir("new_dataset/cats"):
        mkdir("new_dataset/cats")
    if not path.isdir("new_dataset/dogs"):
        mkdir("new_dataset/dogs")


def load_image(animal):
    '''Collects full size images from the Internet'''
    for i in range(2, 5):
        n = 30 * i
        sleep(30)
        link_yandex = f"https://yandex.ru/images/search?text={animal}&p={str(i)}"
        response = requests.get(link_yandex).text

        img_link = []
        soup = BeautifulSoup(response, "lxml")
        invalid_img_link = soup.find_all("a", class_="serp-item__link")
        for img in invalid_img_link:
            url = re.split("url=", unquote(img.get("href")))[1]
            if "jpg" in url:
                img_link.append(url[:url.rfind("jpg") + 3])
            else:
                img_link.append(url[:url.rfind("jpeg") + 4])

        for link in img_link:
            print(link)
            try:
                sleep(5)
                image = requests.get(link, stream=True).content
                path = f"new_dataset\{animal}\{str(n).zfill(4)}.jpg"
                with open(path, "wb") as file:
                    file.write(image)
                    n += 1
            except:
                continue


def cheking_format(path_to_folder: str):
    images = listdir(path_to_folder)
    for image in images:
        path_to_image = f"{path_to_folder}/{image}"
        if(what(path_to_image) != "jpeg"):
            remove(path_to_image)


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
            if np.all(img_data[i] == img_data[j]):
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


def rename_image(path_to_folder: str) -> None:
    '''Changing the name of images'''
    images = listdir(path_to_folder)
    for i, image in enumerate(images):
        before = f"{path_to_folder}/{image}"
        after = f"{path_to_folder}/{str(i).zfill(4)}.jpg"
        rename(before, after)