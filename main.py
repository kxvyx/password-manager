from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ---------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
  password_list = []

  password_list = [random.choice(letters) for char in range(random.randint(4,5))]
  password_list+= [random.choice(symbols) for char in range(random.randint(1,3))]
  password_list+= [random.choice(numbers) for char in range(random.randint(1,2))]
  
  random.shuffle(password_list)
  string=''.join(password_list)

  password_entry.insert(0,string=string)




# ---------------------------- SAVE PASSWORD ----------------------#


def save():
  website_data = website_entry.get()
  email_data = email_entry.get()
  password_data = password_entry.get()
  new_data = {
    website_data:
    {"email": email_data,
    "password": password_data}
  }

  if len(website_data)==0 or len(email_data)==0 or len(password_data) == 0:
    messagebox.showerror(title="ERROR",message="Please do not leave any fields empty!")

  else:
    is_ok = messagebox.askokcancel(message=f"website : {website_data}\nemail : {email_data}\npassword : {password_data}\ndo you want to save the above information?")

    if is_ok:
      try:
        with open("data.json", "r") as file:
          data = json.load(file)
          
#json file didnt run in read mode when it was empty
      except FileNotFoundError:
        with open("data.json", "w") as file:
          json.dump(new_data, file, indent=4)
        
      else:
        data.update(new_data)
        with open("data.json", "w") as file:
          json.dump(data, file, indent=4)
      finally:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
  
#---------------------------search function------------------------#

#IMP: you cant use double quotes inside f string

def search_password():
  website_data = website_entry.get()
  try:
    with open("data.json", 'r') as file:
      data_dict = json.load(file)
  except FileNotFoundError:
    messagebox.showerror(title="Note",message="No information added yet.")
      
  else: 
    if website_data in data_dict.keys():
      messagebox.showinfo(title=website_data,message=f"email:{data_dict[website_data]['email']}\npassword:{ data_dict[website_data]['password']}")
      #print(f"email:{data_dict[website_data]['email']}\npassword:{ data_dict[website_data]['password']}")
    else:
      messagebox.showerror(title="Error",message="No data found for this website.")
    
      


# ---------------------------- UI SETUP -----------------------------#
#---------------------------create window----------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40,bg="#fff")

#----------------------create canvas and put image-----------------#
canvas = Canvas(width=200,height=200,bg="#fff",highlightthickness=0)

lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)

canvas.grid(column=1,row=0)
#-------------------create labels,buttons,entries------------------#

website=Label(text="Website:",bg="#fff",padx=7,pady=7)
website.grid(column=0,row=1)

website_entry = Entry(width=20,bg="#fff")
website_entry.grid(column=1,row=1,columnspan=1)
website_entry.focus()

email=Label(text="Email/Username:",bg="#fff",padx=7,pady=7)
email.grid(column=0,row=2)

email_entry=Entry(width=38,bg="#fff")
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"kavya@gmail.com")

password=Label(text="Password:",bg="#fff",padx=7,pady=7)
password.grid(column=0,row=3)

password_entry=Entry(width=20,bg="#fff")
password_entry.grid(column=1,row=3,columnspan=1)

#buttons
generate_button= Button(text="Generate Password",bg="#fff",command=generate_password)
generate_button.grid(column=2,row=3,columnspan=1)

add_button=Button(width=35,text="Add",bg="#fff",command=save)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(width=14,text="Search",bg="#fff",command=search_password)
search_button.grid(column=2,row=1,columnspan=1)


window.mainloop()