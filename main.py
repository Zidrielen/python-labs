import utils

def main():
    link_cat="https://yandex.ru/images/search?text=cat"
    link_dog="https://yandex.ru/images/search?text=dog"

    utils.make_dir()
    response = utils.save_html(link_cat)


if __name__ == '__main__':
    main()

