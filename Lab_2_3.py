import os
from random import sample
from pathlib import Path

from Lab_2_2 import create_dir, copy_dataset


def randNames_create_csv(ndp: str) -> None:
    names_list = os.listdir(ndp)
    tmp = sample(range(0, 10001), len(names_list))
    n = ndp.rfind("\\")
    name_csv = f"{ndp[n+1:]}_annotation.csv"
    j = 0

    with open(os.path.join(ndp, name_csv), 'w') as file_csv:
        main_path = os.path.join(str(Path.home()), "python-labs")
        for i in names_list:
            if ".jpg" in i:
                s = os.path.join(ndp, i)
                d = os.path.join(ndp, f'{tmp[j]}.jpg')
                os.rename(s, d)
                abspath = str(Path(main_path, d))
                line = abspath+" "+d+" "+i[0:3]+"\n"
                file_csv.write(line)
                j += 1
            

def run_3() -> None:
    new_dataset_path = create_dir("new_dataset_rand")
    copy_dataset("cat", new_dataset_path)
    copy_dataset("dog", new_dataset_path)
    randNames_create_csv(new_dataset_path)
