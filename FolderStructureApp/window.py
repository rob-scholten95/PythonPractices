from tkinter import *
import os
from dir_template import *

main_dir = [inputs, editing, outputs]
main_dir_names = ['inputs', 'editing', 'outputs']
projectname = ''
disk_dir = 'D:\01-Archviz'

def create_dir(p):
    for i, subdir in enumerate(main_dir):
        for dir_name in subdir:
            full_path = os.path.join(p, main_dir_names[i], dir_name)
            try:
                os.makedirs(full_path, exist_ok=True)
                print("Directory", full_path, "Created")
            except FileExistsError:
                print("Directory", full_path, "already exists")
    exit()

def confirm_button():
    projectname = entry_name.get()
    projectnumber = entry_number.get()
    project_title = projectnumber + ' - ' + projectname 
    create_dir(project_title)
    

root = Tk()
root.title("Tk Example")
root.geometry('600x400')

text_number = Label(root, text="Project Name: ")
text_number.grid(row=0, column=0)

entry_name = Entry(root)

entry_name.grid(row=0, column=1)

text_number = Label(root, text="Project Number: ")
text_number.grid(row=1, column=0)

entry_number = Entry(root)

entry_number.grid(row=1, column=1)

b = Button(root, text='Confirm', command=confirm_button)
b.grid(row=3, column=0, columnspan=2, pady=20)

if __name__ == '__main__':
    root.mainloop()
