from os import mkdir

def make_dir():
    mkdir("dataset")
    mkdir("dataset\cat")
    mkdir("dataset\dog")

def main():
    make_dir()
    