from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import pandas


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Clipboard", message=f'{password} copied to clipboard.')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    if website_input == "" or password_input == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: "
                                                                    f"\n{email_input} \n{password_input} "
                                                          f"\nIs it ok to save?")
        if is_ok:
            with open("passwords.txt", mode="a") as data:
                data.write(f"{website_input},{email_input},{password_input}\n")

            # https://www.geeksforgeeks.org/convert-text-file-to-csv-using-python-pandas/
            dataframe = pandas.read_csv("passwords.txt", header=None)
            dataframe.columns = ["Websites", "Emails", "Passwords"]
            dataframe.to_csv("passwords.csv")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email / Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password (main):")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=4)
website_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=4)
email_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate", width=7, highlightthickness=0, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=4)

# Window Loop
window.mainloop()
