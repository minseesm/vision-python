from tkinter import *
import tkinter.ttk as ttk
import os #os like windows or mac. the code can ask the system for etc
from tkinter import filedialog
from PIL import Image
import tkinter.messagebox as msgbox

root = Tk()
root.title ('JULIE GUI')
root.resizable(True, True)        #x, y  #if y becomes false only the width can be changed



#Top button frame
top_frame = Frame(root)
top_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(top_frame, text="Add Files")
btn_add_file.pack(side='left', padx=5, pady=5)

btn_del_file = Button(top_frame, text="Delete Files")
btn_del_file.pack(side='right', padx=5, pady=5)

# List Frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scr = Scrollbar(list_frame)
scr.pack(side="right", fill="y")

list_img = Listbox(list_frame, selectmode='extension', height=15, yscrollcommand=scr.set)
list_img.pack(fill="both", expand=True, side="left")  #when expand is set to false or just deleted the frame size doesn't change when the gui size is changed
scr.config(command=list_img.yview)

# Save path
path_frame = LabelFrame(root, text="Save Path...")
path_frame.pack(fill="both" )

path_label = Label(path_frame, text="")
path_label.pack(side="left")

def path_browse():
    folder_path = filedialog.askdirectory(initialdir="C://Users\visio\OneDrive\Desktop\Julie\Image_fusion\images")
    if folder_path == "":
        return
    path_label.config(text=folder_path)
    
btn_pass_file = Button(path_frame, text="Browse...", command=path_browse)
btn_pass_file.pack(side='right', padx=5, pady=5)

# Options
opt_frame = LabelFrame(root, text="Options")
opt_frame.pack(padx=5, pady=5)

# Width
label_width = Label(opt_frame, text="Width")
label_width.grid(row="1", column='1')

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(opt_frame, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.grid(row="1", column='2')

# Spacing
label_space = Label(opt_frame, text="Space")
label_space.grid(row="1", column='3')

opt_space = ["None", "Slim", "Normal"]
cmb_space = ttk.Combobox(opt_frame, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.grid(row="1", column='4')

# Extension
label_space = Label(opt_frame, text="Expension")
label_space.grid(row="1", column='5')

opt_ext = ["JPEG", "PNG", "BMP"]
cmb_ext = ttk.Combobox(opt_frame, state="readonly", values=opt_ext, width=10)
cmb_ext.current(0)
cmb_ext.grid(row="1", column='6')

# Progressbar
pro_frame = LabelFrame(root, text="Progress status")
pro_frame.pack(fill="x", padx=5, pady=5)

pro_var = DoubleVar()
progress_bar = ttk.Progressbar(pro_frame, maximum=100, variable=pro_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Bottom Button
bottom_frame = Frame(root)
bottom_frame.pack(side="right", padx=5, pady=5)

btn_close_file = Button(bottom_frame, text="Close", command=root.quit)
btn_close_file.pack(side='right', padx=5, pady=5)

btn_start_file = Button(bottom_frame, text="Start")
btn_start_file.pack(side='right', padx=5, pady=5)



root.mainloop()