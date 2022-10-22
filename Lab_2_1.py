import os

def create_csv(path_dir: str) -> None:
    path_ = os.path.join("dataset", path_dir)
    names = os.listdir(path_)
    with open(os.path.join(path_, f"{path_dir}annotation.csv"), 'w') as file_csv:
        for i in names:
             file_csv.write(os.path.abspath(i) + " " +
                           os.path.join(path_, i) + " " + path_dir + "\n")
    file_csv.close()

def run_1() -> None:
    create_csv("cat")
    create_csv("dog")