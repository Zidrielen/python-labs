from os import mkdir
import requests
import re
from bs4 import BeautifulSoup

def make_dir():
    mkdir("dataset")
    mkdir("dataset\cat")
    mkdir("dataset\dog")

def save_html(link):
    return requests.get(link).text

