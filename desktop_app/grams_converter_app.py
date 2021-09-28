from tkinter import *

window = Tk()


def kg_to_pounds_and_ounces():
    print(entry_field_value.get())
    grams = float(entry_field_value.get())*1000
    pounds = float(entry_field_value.get())*2.20462
    ounces = float(entry_field_value.get())*35.274
    grams_output.delete("1.0", END)
    grams_output.insert(END, grams)
    pounds_output.delete("1.0", END)
    pounds_output.insert(END, pounds)
    ounces_output.delete("1.0", END)
    ounces_output.insert(END, ounces)


kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0)

entry_field_value = StringVar()
entry_field = Entry(window, textvariable=entry_field_value)
entry_field.grid(row=0, column=1)

exec_button = Button(window, text="Convert", command=kg_to_pounds_and_ounces)
exec_button.grid(row=0, column=2)  # rowspan can be also added

grams_output = Text(window, height=1, width=20)
grams_output.grid(row=1, column=0)

pounds_output = Text(window, height=1, width=20)
pounds_output.grid(row=1, column=1)

ounces_output = Text(window, height=1, width=20)
ounces_output.grid(row=1, column=2)

window.mainloop()
