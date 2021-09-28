from tkinter import *

window = Tk()


def km_to_miles():
    print(entry_field_value.get())
    miles = float(entry_field_value.get())*1.6
    text_widget.insert(END, miles)


exec_button = Button(window, text="Convert", command=km_to_miles)
exec_button.grid(row=0, column=0)  # rowspan can be also added

entry_field_value = StringVar()
entry_field = Entry(window, textvariable=entry_field_value)
entry_field.grid(row=0, column=1)

text_widget = Text(window, height=1, width=10)
text_widget.grid(row=0, column=2)

window.mainloop()
