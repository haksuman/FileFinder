import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from file_finder import file_copy_func
from file_list import list_files


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
canvas_tab1 = tk.Canvas(tab1, width=550, height=450, background="lightblue")
canvas_tab1.pack()

canvas_tab2 = tk.Canvas(tab2, width=550, height=450, background="lightblue")
canvas_tab2.pack()


# Tab1
# Add label boxes
tk.Label(canvas_tab1, text="Please input list file path", background="skyblue").place(x=100, y=150)
tk.Label(canvas_tab1, text="Please input source folder path", background="skyblue").place(x=100, y=200)
tk.Label(canvas_tab1, text="Please input target folder path", background="skyblue").place(x=100, y=250)
tk.Label(canvas_tab1, text="Please input file extension", background="skyblue").place(x=100, y=300)
# Copyright
tk.Label(canvas_tab1, text="Created by Haksuman", background="lightblue").place(x=205, y=400)


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
#btn_browse_src_list = tk.Button(canvas_tab1, text="Browse").place(x=440, y=150) # command declaration required for buttons
#btn_browse_src_folder = tk.Button(canvas_tab1, text="Browse").place(x=440, y=220)
#btn_target_folder = tk.Button(canvas_tab1, text="Browse").place(x=440, y=270)


# include function
def fnc_btn_copy_files():
    input_path_src_list = path_src_list.get()
    input_path_src_folder = path_src_folder.get()
    input_path_target_folder = path_target_folder.get()
    input_file_ext = str(txt_file_ext.get())

    file_copy_func(input_path_src_list, input_path_src_folder, input_path_target_folder, input_file_ext)  # calling back function from file_finder.py
    tk.messagebox.showinfo(title="Status Notification", message="Completed!")


# add function button
btn_copy_files = tk.Button(text='Copy files to target location', command=fnc_btn_copy_files)
canvas_tab1.create_window(270, 350, window=btn_copy_files)


# Tab2
# Labels for tab2
tk.Label(canvas_tab2, text="Please input source folder path", background="skyblue").place(x=100, y=150)
tk.Label(canvas_tab2, text="Please input file name for output", background="skyblue").place(x=100, y=200)
# Copyright
tk.Label(canvas_tab2, text="Created by Haksuman", background="lightblue").place(x=205, y=400)

#Entris for tab2
path_src_folder_to_list = tk.Entry(canvas_tab2)  # input box responsible for list of Excel file path
canvas_tab2.create_window(350, 160, window=path_src_folder_to_list )

name_file_list_output = tk.Entry(canvas_tab2)  # input box responsible for source folder path
canvas_tab2.create_window(350, 210, window=name_file_list_output)

# list files function
def fnc_btn_list_files():
    input_path_src_folder_to_list = path_src_folder_to_list.get()
    input_name_file_list_output = name_file_list_output.get() 
    list_files(input_path_src_folder_to_list, input_name_file_list_output)  # calling back function from file_finder.py
    tk.messagebox.showinfo(title="Status Notification", message="Completed!")

# Action button to copy files
btn_list_files = tk.Button(canvas_tab2, text='List files in target location', command=fnc_btn_list_files)
canvas_tab2.create_window(280, 250, window=btn_list_files)






root.mainloop()

