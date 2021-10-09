"""
This program stores book information as follows:
Title, Author, Year, ISBN

User can perform the next activities:
- View all records
- Search an entry
- Add entry
- Delete items
- Close the program
"""

from tkinter import *
import book_store_backend


def view_command():
    main_list.delete(0, END)
    for row in book_store_backend.view():
        main_list.insert(END, row)


def search_command():
    main_list.delete(0, END)
    for row in book_store_backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        main_list.insert(END, row)


def add_command():
    book_store_backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    book_store_backend.delete(selected_tuple[0])


def update_command():
    book_store_backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def get_selected_row(event):
    try:
        global selected_tuple
        if main_list.curselection():
            index = main_list.curselection()[0]
            selected_tuple = main_list.get(index)
            title_entry.delete(0, END)
            title_entry.insert(END, selected_tuple[1])
            author_entry.delete(0, END)
            author_entry.insert(END, selected_tuple[2])
            year_entry.delete(0, END)
            year_entry.insert(END, selected_tuple[3])
            isbn_entry.delete(0, END)
            isbn_entry.insert(END, selected_tuple[4])
    except IndexError:
        pass


window = Tk()

window.wm_title("Book Store")

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

title_text = StringVar()
title_entry = Entry(window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_text = StringVar()
author_entry = Entry(window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_text = StringVar()
year_entry = Entry(window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_text = StringVar()
isbn_entry = Entry(window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

main_list = Listbox(window, height=6, width=60)
main_list.grid(row=2, column=0, rowspan=6, columnspan=2)

ml_scroll_bar = Scrollbar(window)
ml_scroll_bar.grid(row=2, column=2, rowspan=6)

main_list.configure(yscrollcommand=ml_scroll_bar.set)
ml_scroll_bar.configure(command=main_list.yview)

main_list.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text="View all", width=12, command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", width=12, command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

window.mainloop()
