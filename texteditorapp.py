import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def create_file(content='', title='Untitled'):
    global text_area
    text_area = tk.Text(notebook)
    text_area.insert('end', content)
    text_area.pack(fill="both", expand =True)
    notebook.add(text_area,text= title)
    notebook.select(text_area)
    text_area.focus()

def save_file():
    file_path = filedialog.asksaveasfilename()
    try:
        filename = os.path.basename(file_path)
        text_widget =root.nametowidget(notebook.select())
        content =text_widget.get('1.0','end-1c')

        with open(file_path, 'w') as file:
            file.write(content)
    except (AttributeError, FileNotFoundError):
        print('Save operation cancelled')
        return
    
    notebook.tab('current', text=filename)

def open_file():
    file_path =filedialog.askopenfilename()
    try:
        filename =os.path.basename(file_path)

        with open (file_path, 'r') as file:
            content = file.read()
        
    except (AttributeError, FileNotFoundError):
        print('Open operation cancelled.')
        return
    
    create_file(content, filename)

root = tk.Tk()
root.title('Custom Text Editor')
root.option_add('*tearoff', False)
main = ttk.Frame(root)
main.pack(fill='both', expand=True, padx =1, pady =(4,0))

menu_bar = tk.Menu()
root.config(menu=menu_bar) 

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(menu=file_menu, label ='File')
file_menu.add_command(label = 'New', command = create_file, accelerator='Ctrl+n')
file_menu.add_command(label='Save', command=save_file, accelerator='Ctrl+s')
file_menu.add_command(label='Open File', command=open_file, accelerator='Ctrl+o')
notebook = ttk.Notebook(main)
notebook.pack(fill='both',expand=True)

create_file()

root.bind('<Control-n>', lambda event: create_file())
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-s>', lambda event: save_file())

root.mainloop()
