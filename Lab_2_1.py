import os
from pathlib import Path

def create_csv(path_dir: str) -> None:
    path_ = os.path.join("dataset", path_dir)
    names = os.listdir(path_)
    with open(os.path.join(path_, f"{path_dir}_annotation.csv"), 'w') as file_csv:
        for i in names:
            if ".jpg" in i:
                abspath = str(Path(Path.home(), "python-labs", path_, i))
                file_csv.write(abspath+" "+
                               os.path.join(path_, i)+" "+path_dir+"\n")
    file_csv.close()


def run_1() -> None:
    create_csv("cat")
    create_csv("dog")