import tkinter as tk
from tkinter import ttk

def _dialog(input_name: str, title: str, callback, second_name: str | None = None):
        toplevel = tk.Toplevel(width = 100, height = 100)
        toplevel.grab_set()
        toplevel.wm_attributes('-topmost', True)
        toplevel.title(title)
        toplevel.resizable(False, False)
        
        var = tk.StringVar()
        ttk.Entry(toplevel, textvariable = var).grid(row = 2, column = 2, padx = 10, pady = 10)
        ttk.Label(toplevel, text = input_name).grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Label(toplevel, text = title).grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)
        if second_name != None:
            second_var = tk.StringVar()
            ttk.Entry(toplevel, textvariable = second_var).grid(row = 3, column = 2, padx = 10, pady = 10)
            ttk.Label(toplevel, text = second_name).grid(row = 3, column = 1, padx = 10, pady = 10)
        
        def confirm():
            if not var.get():
                return
            toplevel.destroy()
            if second_name != None:
                callback(var, second_var)
            else:
                callback(var)
            
        ttk.Button(toplevel, command = confirm, text = 'Confirm', style = 'Accent.TButton').grid(row = 4, column = 1, columnspan = 2, padx = 10, pady = 10, sticky = tk.NSEW)
        toplevel.mainloop()