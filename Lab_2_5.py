from email import iterators
from os import listdir, path
from csv import reader


class Iterator_1:
    def __init__(self, class_name: str) -> None:
        path_ = path.join("dataset", class_name)
        self.names = listdir(path_)
        names_ = self.names.copy()
        for i in names_:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __iter__(self) -> iterators:
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration


class Iterator_2:
    def __init__(self, class_name: str, name_dir: str) -> None:
        path_ = path.join("dataset", name_dir)
        self.names = listdir(path_)
        names_ = self.names.copy()
        for i in names_:
            if not class_name in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __iter__(self) -> iterators:
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration


class Iterator_3:
    def __init__(self, class_name: str, name_dir: str) -> None:
        path_ = path.join("dataset", name_dir)
        self.path_img = []

        with open(path.join(path_, "new_dataset_rand_annotation.csv")) as File:
            reader_ = reader(File, delimiter=" ")
            for it in reader_:
                if it[2] == class_name:
                    self.path_img.append(it[1])
        
        self.limit = len(self.path_img)
        self.counter = 0

    def __iter__(self) -> iterators:
        return self

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return self.path_img[self.counter - 1]
        else:
            raise StopIteration


def run_5() -> None:
    it_1 = Iterator_1("dog")
    for i in it_1:
        print(path.join("dataset", "dog", i))
    
    it_2 = Iterator_2("cat", "new_dataset")
    for i in it_2:
        print(path.join("dataset", "new_dataset", i))
    
    it_3 = Iterator_3("dog", "new_dataset_rand")
    for i in it_3:
        print(i)
