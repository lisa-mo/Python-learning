import os
import init


def main():
    pass


if __name__ == '__main__':
    init_data = init.GetIniTDataClass()
    books_data = init_data.get_init_data("file path")

    main()
