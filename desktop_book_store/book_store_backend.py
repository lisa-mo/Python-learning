import sqlite3


def connect():
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY, title text, author text, year integer, "
                "isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    all_rows = cur.fetchall()
    conn.close()
    return all_rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    all_rows = cur.fetchall()
    conn.close()
    return all_rows


def delete(book_id):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE book_id=?", (book_id, ))
    conn.commit()
    conn.close()


def update(book_id, title="", author="", year="", isbn=""):
    conn = sqlite3.connect("book_store.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE book_id=?", (title, author, year, isbn,
                                                                                       book_id))
    conn.commit()
    conn.close()
