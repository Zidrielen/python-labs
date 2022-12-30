import os


def class_img(animal: str, names_list: list, n: int) -> str:
    '''Specifies the image class'''
    if animal == "cat" or animal == "dog":
        return animal
    else:
        return (names_list[n])[0:3]


def create_csv(path_to_csv: str, path_fol: str, animal: str) -> None:
    '''Creates a csv file for items 1 and 2 of Lab №2'''
    path_ = os.path.join(path_fol, animal)
    names_list = os.listdir(path_)
    
    with open(path_to_csv, 'a') as file_csv:
        for index, image in enumerate(names_list):
            if ".jpg" in image:
                abspath = os.path.join(path_, image)
                class_ = class_img(animal, names_list, index)
                rel_path = os.path.join(animal, image)
                line = abspath + " " + rel_path + " " + class_ + "\n"
                file_csv.write(line)