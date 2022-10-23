from os import listdir, path

class Iterator:
    def __init__(self, name: str):
        path_ = path.join("dataset", name)
        self.names = listdir(path_)
        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            raise StopIteration


def run_5() -> None:
    it = Iterator("dog")
    for i in it:
        print(path.join("dataset", "dog", i))