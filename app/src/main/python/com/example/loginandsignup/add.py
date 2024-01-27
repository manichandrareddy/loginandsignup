Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import tkinter as tk
... 
... class Add(tk.Tk):
...     def __init__(self):
...         super().__init__()
...         self.title("Activity Add")
... 
...         # You would add your widgets here to set up your layout
...         # For example, a label:
...         label = tk.Label(self, text="This is the Add activity")
...         label.pack()
... 
... # To run the application, you would do something like this:
... if __name__ == "__main__":
...     app = Add()
...     app.mainloop()
... 
... 
