from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

with open("1000_most_common_passwords.txt") as data_file:
    data = data_file.readlines()
    common_passwords = [datum.strip() for datum in data]


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password = [char for char in password_letters + password_numbers + password_symbols]
    shuffle(password)
    generated_password = "".join(password)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def capital_letter_exists(string):
    for char in string:
        if char == char.upper():
            return True


def symbol_exists(string):
    for char in string:
        if char in symbols:
            return True


def number_exists(string):
    for char in string:
        if char.isdigit():
            return True


def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if (len(website) < 1) or (len(password) < 1) or (len(username) < 1):
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")
    elif password in common_passwords:
        pwd_validity_label1.grid_remove()
        add_button.grid(row=5, column=1)
        pwd_validity_label2.grid(row=4, column=1)
    elif (len(password) < 8) or (not capital_letter_exists(password)) or (not symbol_exists(password)) \
            or (not number_exists(password)):
        add_button.grid(row=5, column=1)
        pwd_validity_label2.grid_remove()
        pwd_validity_label1.grid(row=4, column=1, columnspan=6)
    else:
        pwd_validity_label1.grid_remove()
        pwd_validity_label2.grid_remove()
        add_button.grid(row=4, column=1)
        is_ok = messagebox.askokcancel(title=f"Website: {website}",
                                       message=f"These are the details entered: \nEmail: {username} \n"
                                               f"Password: {password} \nIs it ok to save?😤")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website}  |  {username}  |  {password}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.insert(END, "example@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

pwd_validity_label1 = Label(text="**Password must contain 8 characters (including at least \none capital letter and a "
                                 "special character)🥴                               ",
                            fg="red")
pwd_validity_label2 = Label(text="**Password is too common boss 🤲🏾", fg="red")

# Inputs
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(END, "example@gmail.com")

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

#  Buttons
gen_pwd_button = Button(text="Generate Password", command=generate_password)
gen_pwd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
