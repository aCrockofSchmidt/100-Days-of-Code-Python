import tkinter

# create main window

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=15, pady=15)
# window.minsize(width=300, height=150)


def conversion():
    submission = round(float(user_input.get()) * 1.60934, 2)
    answer_label.config(text=submission)


# create button

calc_button = tkinter.Button(text="Calculate", command=conversion)
calc_button.grid(column=1, row=2)


# create input

user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)


# create labels

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = tkinter.Label()
answer_label.grid(column=1, row=1)

text_label = tkinter.Label(text="is equal to")
text_label.grid(column=0, row=1)






window.mainloop()