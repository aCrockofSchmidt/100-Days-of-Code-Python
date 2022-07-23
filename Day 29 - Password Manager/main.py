from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))] \
                    + [random.choice(symbols) for sym in range(random.randint(2, 4))] \
                    + [random.choice(numbers) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered. \n\nEmail: {user_email}"
                                                       f"\nPassword: {user_password}\n\nIs it OK to save?")
        if is_ok:

            combined_entry = f"{user_website} | {user_email} | {user_password}\n"

            with open("data.txt", "a") as data_file:
                data_file.write(combined_entry)

            website_input.delete(0, END)
            website_input.focus()
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# inputs

website_input = Entry(width=54)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=54)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "fake_email@gmail.com")

password_input = Entry(width=36)
password_input.grid(column=1, row=3)

# buttons

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
