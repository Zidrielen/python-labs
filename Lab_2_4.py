from os import listdir, path
from typing import Optional


def iterator(name: str) -> Optional[str]:
    path_ = path.join("dataset", name)
    names = listdir(path_)
    for i in range(len(names)):
        if ".jpg" in names[i]:
            path_file = path.join(path_, names[i])
            yield (path_file)
    return None


def run_4() -> None:
    it = iterator("cat")
    for i in it:
        print(i)