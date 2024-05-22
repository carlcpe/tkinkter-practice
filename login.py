import sqlite3
import customtkinter  as ctk
from tkinter import *
from tkinter import messagebox 


class LoginApp():
    def __init__(self):
        self.login_window = ctk.CTk()
        self.login_window.title("Login")
        self.login_window.geometry("320x240")

        ctk.CTkLabel(self.login_window, text="Username").pack()
        self.username_entry = ctk.CTkEntry(self.login_window)
        self.username_entry.pack()

        ctk.CTkLabel(self.login_window, text="Password").pack()
        self.password_entry = ctk.CTkEntry(self.login_window, show="*")
        self.password_entry.pack()

        self.login_button = ctk.CTkButton(self.login_window, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.login_window.mainloop()
    
    def login(self):
        conn = sqlite3.connect('user_db.db')
        cursor = conn.cursor()

        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?;", (username, password))
        user = cursor.fetchone()

        if user:
            self.show_profile(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or Password")
        
        conn.close()

    def show_profile(self, user):
        self.login_window.destroy()
        self.profile_window = ctk.CTk()
        self.profile_window.geometry("320x240")
        self.profile_window.title(f'Profile of {user[0]}')

        ctk.CTkLabel(self.profile_window, text=f'Name: {user[2]}').pack()
        ctk.CTkLabel(self.profile_window, text=f'Age: {user[3]}').pack()
        ctk.CTkLabel(self.profile_window, text=f'Email: {user[4]}').pack()

        self.profile_window.mainloop()
        

if __name__ == '__main__':
    LoginApp()