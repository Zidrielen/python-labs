from time import sleep
from os import mkdir

import requests
from bs4 import BeautifulSoup

LINK_YANDEX="https://yandex.ru/images/search?text="
LINK_PART_2="&p="
DOG="dog"
CAT="cat"

def make_dir():
    mkdir("dataset")
    mkdir("dataset\cat")
    mkdir("dataset\dog")


def save_html(link):
    return requests.get(link).text


def load_image(link):
    return requests.get(link, stream=True).content


def save_image(response, animal, n):
    soup = BeautifulSoup(response, "lxml")
    all_link_tag_img = soup.find_all("img", class_="serp-item__thumb justifier__thumb")
    for link_tag_img in all_link_tag_img:
        sleep(10)
        image = load_image("http:" + link_tag_img.get("src"))
        name = str(n).zfill(4)
        path = f"dataset\{animal}\{name}.jpg"
        file = open(path, "wb")
        file.write(image)
        file.close()
        n += 1
        

def push_image(animal):
    for i in range(0, 37):
        n = 30 * i
        sleep(30)
        response = save_html(LINK_YANDEX + animal + LINK_PART_2 + str(i))
        save_image(response, animal, n)


def main():
    #Make directories for images
    make_dir()

    #Add images in "cat" directory
    push_image(CAT)

    #Add images in "dog" directory
    push_image(DOG)