import tkinter as tk
from tkinter import ttk

def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand =True)
    notebook.add(text_area,text='Untitled')
    notebook.select(text_area)
    text_area.focus()

root = tk.Tk()
root.title('Custom Text Editor')
root.option_add('*tearoff', False)
main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx =1, pady =(4,0))

menu_bar = tk.Menu()
root.config(menu=menu_bar) 

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(menu=file_menu, label ='File')
file_menu.add_command(label = 'new', command = create_file)

notebook = ttk.Notebook(main)
notebook.pack(fill='both',expand=True)

create_file()

root.mainloop()
