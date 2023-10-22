import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pack Exercise!")

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)
label1 = tk.Label(main, text='Label 1', bg='green')
label2 = tk.Label(main, text='Label 2', bg = 'red')
label1.pack(side='left', fill= 'both', expand =True)
label2.pack(side='top', fill ='both', expand=True)
label3 = tk.Label(root, text='Label 3', bg = 'green')
label3.pack(side='left', fill ='both', expand=True)



tk.mainloop()