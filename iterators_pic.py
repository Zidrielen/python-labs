from os import listdir, path
from typing import Optional
from email import iterators
from csv import reader


def iterator(class_name: str) -> Optional[str]:
    '''Function "iterator" for item 4 of laboratory No. 2'''
    path_ = path.join("dataset", class_name)
    names = listdir(path_)
    for i in range(len(names)):
        if ".jpg" in names[i]:
            path_file = path.join(path_, names[i])
            yield (path_file)
    return None


class Iterator_1:
    '''Iterates images from source dataset'''
    def __init__(self, full_path: str, class_name: str) -> None:
        '''Constructor'''
        self.path_ = path.join(full_path, class_name)
        self.names = listdir(self.path_)
        names_ = self.names.copy()
        for i in names_:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __iter__(self) -> iterators:
        '''For iterating in a for loop'''
        return self

    def __next__(self) -> str:
        '''Returning an iterator and moving on to the next one'''
        if self.counter < self.limit:
            self.counter += 1
            return path.join(self.path_, self.names[self.counter - 1])
        else:
            raise StopIteration


class Iterator_2:
    '''iterating images organized as in item 2'''
    def __init__(self, full_path: str, class_name: str) -> None:
        '''Constructor'''
        self.path_to_folder = full_path
        self.names = listdir(full_path)
        names_ = self.names.copy()
        for i in names_:
            if not class_name in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __iter__(self) -> iterators:
        '''For iterating in a for loop'''
        return self

    def __next__(self) -> str:
        '''Returning an iterator and moving on to the next one'''
        if self.counter < self.limit:
            self.counter += 1
            return path.join(self.path_to_folder, self.names[self.counter - 1])
        else:
            raise StopIteration


class Iterator_3:
    '''iterating images organized as in item 3'''
    def __init__(self, full_path: str, class_name: str) -> None:
        '''Constructor'''
        self.path_img = []

        with open(path.join(full_path, "annotation.csv")) as File:
            reader_ = reader(File, delimiter=" ")
            for it in reader_:
                if it[2] == class_name:
                    self.path_img.append(it[0])
        
        self.limit = len(self.path_img)
        self.counter = 0

    def __iter__(self) -> iterators:
        '''For iterating in a for loop'''
        return self

    def __next__(self) -> str:
        '''Returning an iterator and moving on to the next one'''
        if self.counter < self.limit:
            self.counter += 1
            return self.path_img[self.counter - 1]
        else:
            raise StopIteration