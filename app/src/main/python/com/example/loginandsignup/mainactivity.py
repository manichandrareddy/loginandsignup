Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Importing necessary libraries
from tkinter import Tk, Button
import webbrowser

class MainActivity:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Activity")
... 
...         # Creating buttons
...         self.order_details_btn = Button(master, text="Order Details", command=self.open_order_details)
...         self.order_details_btn.pack()
... 
...         self.combo_btn = Button(master, text="Combo", command=self.open_combo)
...         self.combo_btn.pack()
... 
...         self.add_btn = Button(master, text="Add", command=self.open_add)
...         self.add_btn.pack()
... 
...         self.logout_btn = Button(master, text="Logout", command=self.logout)
...         self.logout_btn.pack()
... 
...     def open_order_details(self):
...         # Simulate opening a new activity
...         webbrowser.open("http://example.com/orderDetails")
... 
...     def open_combo(self):
...         # Simulate opening a new activity
...         webbrowser.open("http://example.com/Combo")
... 
...     def open_add(self):
...         # Simulate opening a new activity
...         webbrowser.open("http://example.com/add")
... 
...     def logout(self):
...         # Simulate logging out
...         print("Logged out")
...         # Simulate starting a new activity (Login)
...         webbrowser.open("http://example.com/Login")
... 
... # Create the main window
... root = Tk()
... app = MainActivity(root)
... root.mainloop()
...  note
... 
