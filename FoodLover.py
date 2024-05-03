from tkinter import filedialog
from PIL import Image, ImageTk
import customtkinter 

test_email = "jonnymoreira03@hotmail.com"
testpw = "Password"


def newwin(): # cleans screen and loads new window once prompted
    for widget in root.winfo_children():
        widget.destroy()


def mainscreen(): #main screen where users can sign up or register
    newwin()
    fl_logo = ImageTk.PhotoImage(Image.open("Images/food_lover.ico").resize((100,100), Image.Resampling.LANCZOS))
    customtkinter.CTkLabel(root, image=fl_logo, text="", bg_color="white").place(relx=0.47, rely= 0.32)
    customtkinter.CTkLabel(root, text=" Welcome to Food Lover", compound="left",font=("Futura", 20, "bold"),justify="center", text_color="black", bg_color="white").place(relx=0.40, rely= 0.5)
    register_btn = customtkinter.CTkButton(root, text="Register", command= register, fg_color="black", text_color="white", hover_color="grey", font=("Futura",15), border_color='white')
    register_btn.place(anchor='center', relx=0.52, rely=0.66)

    login_btn = customtkinter.CTkButton(root, command= login,text="Login", fg_color="black", text_color="white", hover_color="grey", font=("Futura",15), corner_radius=10)
    login_btn.place(anchor='center', relx=0.52, rely=0.6)

    customtkinter.CTkLabel(root, text="Copyright: Team F", font=("Futura", 10, "bold"), text_color="black", bg_color="white").place(relx= .48, rely=0.95)


def login(): #login window
    newwin()
    btn = customtkinter.CTkImage(Image.open("Images/arrow.png"),size=(26, 26))
    register_btn = customtkinter.CTkButton(master=root, image=btn, command=mainscreen, text="", fg_color="white", hover=False)
    register_btn.place(relx=0, rely=0.01)

    customtkinter.CTkLabel(root, text=" Welcome back", compound="left",font=("Futura", 25, "bold"), text_color="black", bg_color="white").place(relx=0.42, rely= 0.3)

    email_entry = customtkinter.CTkEntry(root, placeholder_text="Email", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    email_entry.place(relx=0.4, rely=0.4)

    pw_entry = customtkinter.CTkEntry(root, placeholder_text="Password", show="*", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    pw_entry.place(relx=0.4, rely=0.45)

    customtkinter.CTkButton(root, command= lambda:enterPassword(email_entry.get(), pw_entry.get()), text="Enter", fg_color='black', text_color="white").place(rely=0.52, relx=0.45)
    
def register():
    newwin()
    btn = customtkinter.CTkImage(Image.open("Images/arrow.png"),size=(26, 26))
    register_btn = customtkinter.CTkButton(master=root, image=btn, command=mainscreen, text="", fg_color="white", hover=False)
    register_btn.place(relx=0, rely=0.01)
    customtkinter.CTkLabel(root, text="Hello new user !!!", compound="left",font=("Futura", 25, "bold"), text_color="black", bg_color="white").place(relx=0.40, rely= 0.32)

    name_entry = customtkinter.CTkEntry(root, placeholder_text="Name", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    name_entry.place(relx=0.4, rely=0.4)

    email_entry = customtkinter.CTkEntry(root, placeholder_text="Email", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    email_entry.place(relx=0.4, rely=0.45)

    password_entry = customtkinter.CTkEntry(root, placeholder_text="Password", width=250, placeholder_text_color="grey", text_color="black", fg_color="white")
    password_entry.place(relx=0.4, rely=0.5)

    customtkinter.CTkButton(root, text="Enter", fg_color='black', text_color="white").place(relx=0.45, rely=0.55)


    

def enterPassword(email, pw):
    if test_email == email and testpw == pw:
        newwin()
        customtkinter.CTkLabel(root, text="HELLO USER", compound="left",font=("Futura", 20, "bold"),justify="center", text_color="black", bg_color="white").place(relx=0.44, rely= 0.5)
    else:
        customtkinter.CTkLabel(root, text=" No User Found", compound="left",font=("Futura", 20, "bold"),justify="center", text_color="black", bg_color="white").place(relx=0.44, rely= 0.6)



# attributes of app
root = customtkinter.CTk()
root.geometry("1080x720")
root.title("Food Lover")
root.minsize(1080,720)
root.iconphoto(False,ImageTk.PhotoImage(Image.open("Images/food_lover.ico")))
root.config(bg="white")

mainscreen()

root.mainloop()
