from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passw_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    passw_symbol = [random.choice(symbols) for i in range(random.randint(2, 4))]
    passw_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    passw = passw_letters + passw_symbol + passw_numbers

    random.shuffle(passw)
    passw_final = "".join(passw)
    if len(passw_ent.get()) != 0:
        passw_ent.delete(0, END)
    passw_ent.insert(END, passw_final)
    pyperclip.copy(passw_final)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_ent.get()
    email = email_ent.get()
    passw = passw_ent.get()
    new_data = {
        website: {
            "email" : email,
            "password" : passw
        }
    }

    if len(website) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showwarning(title="Oops", message="One of the filled is empty, please fill out all fields!")
    else:
        is_ok = messagebox.askokcancel("website",message=f"These are the details entered: "
                            f"\nEmail: {email}"
                            f"\nPassword: {passw}"
                            f"\nWebsite: {website}"
                            f"\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    #Read data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", mode="w") as file:    
                    #Write data
                    json.dump(new_data, file, indent=4)
            else:
                #Update data
                data.update(new_data)
                with open("data.json", mode="w") as file:    
                    #Write data
                    json.dump(data, file, indent=4)
            finally:
                website_ent.delete(0, "end")
                passw_ent.delete(0, "end")

# ----------------------------- SEARCH -------------------------------- #
                
def search():
    is_data_saved = False
    if len(website_ent.get()) == 0:
        messagebox.showerror(title="Oops", message="Please fill out the website entry.")
    else:
        try:
            with open("data.json", mode="r") as file:
                saved_data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Oops", message="There is no saved data yet")
        else: 
            for key in saved_data:
                if website_ent.get().lower() == key.lower():
                    is_data_saved = True
        finally:
            if is_data_saved:
                messagebox.showinfo(title=key, message=f"Email: {saved_data[key]["email"]}\nPassword: {saved_data[key]["password"]}")
            else:
                messagebox.showinfo(title="Oops", message=f"There is no '{website_ent.get()}' saved.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

#Creating lock image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#TODO Label creation
wewsite_lbl = Label(text="Website:")
wewsite_lbl.grid(column=0, row=1)

email_lbl = Label(text="Email/Username:")
email_lbl.grid(column=0, row=2)

passw_lbl = Label(text="Passworld:")
passw_lbl.grid(column=0, row=3)

#TODO Button creation
gen_passw_but = Button(text="Generate Password", command=generate_password)
gen_passw_but.grid(column=2, row=3, sticky="EW")

add_but = Button(text="Add", command=save_data)
add_but.grid(column=1, row=4, columnspan=2, sticky="EW")

search_but = Button(text="Search", command=search)
search_but.grid(column=2, row=1, sticky="EW")


#TODO Entries
website_ent = Entry()
website_ent.grid(column=1, row=1, sticky="EW")

email_ent = Entry()
email_ent.grid(column=1, row=2, columnspan=2, sticky="EW")
email_ent.insert(END, "valami@valami.com")
email_ent.focus()

passw_ent = Entry()
passw_ent.grid(column=1, row=3, sticky="EW")

window.mainloop()