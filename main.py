from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    from random import randint, choice, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #new_list=[item for item in range()


    password_letter = [choice(letters) for item in range(randint(8, 10))]
    password_symbol = [choice(symbols) for item in range(randint(2, 4))]
    password_number = [choice(numbers) for item in range(randint(2, 4))]

    password_list = password_number+password_symbol+password_letter

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    wbsite = website_entry.get()
    email = email_username_entry.get()
    made_password = password_entry.get()

    if len(wbsite) == 0 or len(email) == 0 or len(made_password) == 0:
        messagebox.showinfo(title="Oppps",message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=wbsite, message=f'These are the details entered: \n'
                                                            f'Email: {email}\n'
                                                            f'Password: {made_password}\n'
                                                            f'Is it ok to save?')
        if is_ok:

            with open('data.txt', 'a') as data_file:
                data_file.write(f'Website:{wbsite}  ||   Password:{made_password}\n')


            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Passward Manager')
window.config(padx=50, pady=50)

canvas = Canvas()
canvas.config(height=200, width=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#Labels

website = Label(text='Website:')
website.grid(row=1, column=0)
email_username = Label(text='Email/Username:')
email_username.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'shafin73@student.sust.edu')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
generate_password_button = Button(text='Generate Password', width=15, command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()