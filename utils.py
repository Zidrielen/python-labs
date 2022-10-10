from time import sleep
from os import mkdir, replace, listdir
from imghdr import what

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


def remove_stranger(animal, stranger):
    mkdir(f"dataset\stranger_{animal}")

    for image in stranger:
        sourse = f"dataset\{animal}\{image}"
        destination = f"dataset\stranger_{animal}\{image}"
        replace(sourse, destination)
        #Instead of the lines above should be this
        #remove(f"dataset\dog\{image}")


def cheking_format(animal):
    non_jpg_dir = f"dataset/non_jpg_format_{animal}"
    mkdir(non_jpg_dir)

    images = listdir(f"dataset\{animal}")
    for image in images:
        path = f"dataset\{animal}\{image}"
        if(what(path) != "jpeg"):
            replace(path, non_jpg_dir + "/" + image)
            #Instead of the lines above should be this
            #remove(path)      


def main():
    #Make directories for images
    make_dir()

    #Add images in "cat" directory
    push_image(CAT)

    #Add images in "dog" directory
    push_image(DOG)

    #Deleting "foreign" images in the "dog" folder
    stranger_dog = ["0271.jpg", "0318.jpg", "0338.jpg", "0522.jpg", "0559.jpg",
                    "0383.jpg", "0420.jpg", "0508.jpg", "0547.jpg", "0561.jpg",
                    "0129.jpg", "0149.jpg", "0154.jpg", "0167.jpg", "0567.jpg",
                    "0202.jpg", "0235.jpg", "0262.jpg", "0382.jpg", "0574.jpg",
                    "0607.jpg", "0624.jpg", "0646.jpg", "0672.jpg", "0698.jpg",
                    "0709.jpg", "0726.jpg", "0737.jpg", "0786.jpg", "0816.jpg",
                    "0828.jpg", "0843.jpg", "0855.jpg", "0881.jpg", "0942.jpg",
                    "1022.jpg", "1029.jpg", "1065.jpg", "1072.jpg", "1082.jpg",
                    "1089.jpg", "1096.jpg"]
    remove_stranger(DOG, stranger_dog)

    #Deleting "foreign" images in the "cat" folder
    stranger_cat = ["0410.jpg", "0772.jpg", "0782.jpg", "0911.jpg", "0977.jpg"]
    remove_stranger(CAT, stranger_cat)

    #Checking for .jpg format
    cheking_format(CAT)
    cheking_format(DOG)
    #all images are in jpg format
    