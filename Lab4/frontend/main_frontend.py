from tkinter import *
import tkinter as tk
import os
import sys
import matplotlib.pyplot as plt
 
# adding Folder_2 to the system path
sys.path.append("..")

import __init__
from Lab4.backend.main_backend import Manage_Circuit
# root window
window = Tk()
window.title("Biểu diễn và tính điện trở của mạch")
t=800
W,H = t,3*t//5
window.geometry(f'{W}x{H}')
input_frame = Frame(master=window,width=W, height=H*3/8)
output_frame = Frame(master=window,width=W, height=H*5/8)

rela_frame = Frame(master=input_frame,width=W, height=H/8)

lable_rela_frame=Frame(master=rela_frame,width=W, height=H/16,pady=2)
value_rela_frame=Frame(master=rela_frame,width=W, height=H/16,pady=2)

value_output_frame = Frame(master=output_frame,width=W,height=(H*5/8)*1/10)
image_output_frame = Frame(master=output_frame,width=W,height=(H*5/8)*9/10)
lbl_value_output = tk.Label(master=value_output_frame,justify=tk.LEFT)

#download_icon = tk.PhotoImage(file=os.path.join(os.getcwd(),'frontend/images/plot_circuit.png'))
lbl_image_output = tk.Label(master=image_output_frame, justify=tk.CENTER,)

button_frame = Frame(master=input_frame, width=W/4, height=H/16)
#------------------------------------------
lbl_circuit = tk.Label(master=lable_rela_frame, text="Mô tả mạch điện",justify=tk.LEFT,width=W//37, padx=5)
ent_circuit = tk.Entry(master=lable_rela_frame,width=W*4//5)

lbl_value = tk.Label(master=value_rela_frame, text="Giá trị các thành phần",justify=tk.LEFT,width=W//37,padx=5)
ent_value = tk.Entry(master=value_rela_frame,width=W*4//5)

def click_button():
    print("Button has been clicked")
    circuit = ent_circuit.get()
    value_circuit = ent_value.get()
    print(f"circuit:{circuit}")
    print(f"value_circuit:{value_circuit}")
    circuit = "R1*(R2+(R3*R4))"
    value_circuit="R1=3,R2=4,R3=5,R4=6"
    if circuit!="" and value_circuit!="":
        backend = Manage_Circuit(circuit,value_circuit)
        download_icon = backend.get_draw()[-1]
        print(f"path = {download_icon}")
        a = PhotoImage(file=download_icon)
        print(a)
        plt.imshow(a)
        lbl_image_output["image"] = a
        lbl_value_output["text"] = f"Giá trị của điện trở tương đương:  {backend.get_R()}"

button_show = tk.Button(master= button_frame, command=click_button, text="Biểu diễn")


#----------------------------------------------------
input_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
output_frame.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
rela_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)

lbl_circuit.pack(side=tk.LEFT,fill=tk.BOTH)
lbl_value.pack(side=tk.LEFT,fill=tk.BOTH)
ent_circuit.pack(side=tk.LEFT,fill=tk.BOTH)
ent_value.pack(side=tk.LEFT,fill=tk.BOTH)

lable_rela_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
value_rela_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
button_frame.pack(expand=True)
button_show.pack(fill=tk.BOTH,side=tk.TOP,expand=True)

value_output_frame.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
image_output_frame.pack(fill=tk.BOTH,side=tk.TOP, expand=True)

lbl_value_output.pack(fill=tk.BOTH,expand=True)
lbl_image_output.pack(fill=tk.BOTH,expand=True)

window.mainloop()
