import tkinter as tk
from tkinter import ttk
from file_finder import file_copy_func


root = tk.Tk()
root.title("FileFinder")


# Tab control
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="File Locator")
tab_control.add(tab2, text="File Lister")
tab_control.pack(expand = 1, fill ="both")



# Create Canvas
canvas_tab1 = tk.Canvas(tab1, width=650, height=450, background="lightblue")
canvas_tab1.pack()

canvas_tab2 = tk.Canvas(tab2, width=650, height=450, background="lightblue")
canvas_tab2.pack()


# Tab1
# Add label boxes
tk.Label(canvas_tab1, text="Please input list file path", background="skyblue").place(x=100, y=150)
tk.Label(canvas_tab1, text="Please input source folder path", background="skyblue").place(x=100, y=200)
tk.Label(canvas_tab1, text="Please input target folder path", background="skyblue").place(x=100, y=250)
tk.Label(canvas_tab1, text="Please input file extension", background="skyblue").place(x=100, y=300)


# Add entry boxes
path_src_list = tk.Entry(canvas_tab1)  # input box responsible for list of Excel file path
canvas_tab1.create_window(350, 160, window=path_src_list)

path_src_folder = tk.Entry(canvas_tab1)  # input box responsible for source folder path
canvas_tab1.create_window(350, 210, window=path_src_folder)

path_target_folder = tk.Entry(canvas_tab1)  # input box responsible for target folder path
canvas_tab1.create_window(350, 260, window=path_target_folder)

txt_file_ext = tk.Entry(canvas_tab1)  # input box responsible for target folder path
canvas_tab1.create_window(350, 310, window=txt_file_ext)

# Browse buttons
btn_browse_src_list = tk.Button(text="Browse").place(x=440, y=170) # command declaration required for buttons
btn_browse_src_folder = tk.Button(text="Browse").place(x=440, y=220)
btn_target_folder = tk.Button(text="Browse").place(x=440, y=270)


# include function
def fnc_btn_copy_files():
    input_path_src_list = path_src_list.get()
    input_path_src_folder = path_src_folder.get()
    input_path_target_folder = path_target_folder.get()
    input_file_ext = str(txt_file_ext.get())

    file_copy_func(input_path_src_list, input_path_src_folder, input_path_target_folder, input_file_ext)  # calling back function from file_finder.py


# add function button
btn_copy_files = tk.Button(text='Copy files to target location', command=fnc_btn_copy_files)
canvas_tab1.create_window(300, 350, window=btn_copy_files)


# Tab2


root.mainloop()

