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

def add_file():
    files = filedialog.askopenfilenames(title="Select Images",
                                         filetypes=(("JPG File", "*.jpg"),("All Files", "*.*")),
                                         initialdir="C://Users\visio\OneDrive\Desktop\Julie\Image_fusion\images")
    for file in files:
        list_img.insert(END, file)

btn_add_file = Button(top_frame, text="Add Files", command=add_file)
btn_add_file.pack(side='left', padx=5, pady=5)

def del_file():
    for index in reversed(list_img.curselection()):
        list_img.delete(index)

btn_del_file = Button(top_frame, text="Delete Files", command=del_file)
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

path_label = Label(path_frame, text="C://Users\visio\OneDrive\Desktop\Julie\Image_fusion\images")
path_label.pack(side="left")

folder_path = ''
def path_browse():
    global folder_path
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
label_space = Label(opt_frame, text="Extension")
label_space.grid(row="1", column='5')

opt_ext = ["JPG", "PNG", "BMP"]
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

def fusion_images():
    #Option1 - Width
    img_width = cmb_width.get()
    if img_width == "Original":
        img_width = -1
    else:
        img_width = int(img_width)

    #Option2 - Space
    img_space = cmb_space.get()
    if img_space == "None":
        img_space = 0
    elif img_space == "Slim":
        img_space = 30
    elif img_space == "Normal":
        img_space = 60
    
    #Option3 - Extension
    img_ext = cmb_ext.get().lower()

    images = [Image.open(img_path) for img_path in list_img.get(0,END)]


    #Options Apply
    image_size = []   #image_size[0] : width image_size[1] : height

    if img_width > -1:
        image_size = [(int(img_width), int(img_width * x.size[1]/x.size[0])) for x in images]
    else:
        image_size = [(x.size[0], x.size[1]) for x in images]

    widths, height = zip(*(image_size))

    max_width, total_height = max(widths), sum(height)

    if img_space > 0 :
        total_height += (img_space * (len(images) -1 ))

    result_img = Image.new("RGB", (max_width, total_height), (0,0,0))
    y_offset = 0 

    for idx, img in enumerate(images) :
        if img_width > -1:
            img = img.resize(image_size[idx])

        result_img.paste(img, (0,y_offset))
        y_offset += (img.size[1] + img_space)

        progress = (idx +1) / len(images) * 100
        pro_var.set(progress)
        progress_bar.update()

    file_name = "Fusioned_image." + img_ext
    save_path = os.path.join(folder_path, file_name)
    result_img.save(save_path)
    msgbox.showinfo("Notice", "Done")
    
def start():
    # Check the list box
    if list_img.size() == 0:
        msgbox.showwarning("Warning", "Add image files")
        return
    
    # Get Option
    fusion_images()
    #Run

btn_start_file = Button(bottom_frame, text="Start", command=start)
btn_start_file.pack(side='right', padx=5, pady=5)



root.mainloop()