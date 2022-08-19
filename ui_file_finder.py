import tkinter as tk
import tkfilebrowser
from file_finder import file_copy_func


root = tk.Tk()

# Create Canvas
canvas_main = tk.Canvas(root, width=650, height=450)
canvas_main.pack()


# Add label boxes
lbl_list_path = tk.Label(root, text="Please input list file path")
lbl_list_path.place(x=140, y=150)
tk.Label(root, text="Please input source folder path").place(x=140, y=200)
tk.Label(root, text="Please input target folder path").place(x=140, y=250)
tk.Label(root, text="Please input file extension").place(x=140, y=300)

# Add entry boxes
path_src_list = tk.Entry(root)  # input box responsible for list of Excel file path
canvas_main.create_window(400, 160, window=path_src_list)

path_src_folder = tk.Entry(root)  # input box responsible for source folder path
canvas_main.create_window(400, 210, window=path_src_folder)

path_target_folder = tk.Entry(root)  # input box responsible for target folder path
canvas_main.create_window(400, 260, window=path_target_folder)

txt_file_ext = tk.Entry(root)  # input box responsible for target folder path
canvas_main.create_window(400, 310, window=txt_file_ext)

# # browse button
# file = tkfilebrowser.askopenfilename(parent=root, mode='rb', title='Choose a file')
# if file:
#     data = file.read()
#     file.close()
#     print("OK")

# include function
def fnc_btn_copy_files():
    input_path_src_list = path_src_list.get()
    input_path_src_folder = path_src_folder.get()
    input_path_target_folder = path_target_folder.get()
    input_file_ext = str(txt_file_ext.get())

    file_copy_func(input_path_src_list, input_path_src_folder, input_path_target_folder, input_file_ext)  # calling back function from file_finder.py


# add function button
btn_copy_files = tk.Button(text='Copy files to target location', command=fnc_btn_copy_files)
canvas_main.create_window(300, 350, window=btn_copy_files)

root.mainloop()
