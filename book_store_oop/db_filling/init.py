import os

class GetIniTDataClass():

    def __init__(self):
        self.title_key = "title"
        self.author_key = "author"
        self.year_key = "year"
        self.isbn_key = "isbn"
        # dict format
        self.books_init_data = {"title": None, "author": None, "year": None, "isbn": None}

    def get_init_data(self, file_path):
        self.books_init_data[self.title_key] = None
        self.books_init_data[self.author_key] = None
        self.books_init_data[self.year_key] = None
        self.books_init_data[self.isbn_key] = None
        return self.books_init_data
