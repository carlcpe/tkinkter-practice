import customtkinter  as ctk
from tkinter import *
import login as lg
import register as rg

class WelcomeScreen():
    def __init__(self):
        self.welcome_window = ctk.CTk()
        self.welcome_window.title("Welcome!")
        self.welcome_window.geometry("320x240")

        ctk.CTkLabel(self.welcome_window, text="Welcome to my Landing Page!").pack(padx=10, pady=10)
        login_button = ctk.CTkButton(self.welcome_window, text="Login", command=self.pressed_login)
        login_button.pack(pady=10)

        register_button = ctk.CTkButton(self.welcome_window, text="Register", command=self.pressed_register)
        register_button.pack(pady=10)

        self.welcome_window.mainloop()

    def pressed_login(self):
        self.welcome_window.destroy()
        lg.LoginApp()
    
    def pressed_register(self):
        self.welcome_window.destroy()
        rg.RegisterApp()
    

if __name__ == '__main__':
    WelcomeScreen()
