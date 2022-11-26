from tkinter import *

w = Tk()
w.title("Biểu diễn và tính điện trở của mạch")
W,H = 300,150
w.geometry(f'{W}x{H}')

input_frame = Frame(w)
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

circuit = StringVar()
values = StringVar()

# email
circuit_label = Label(w, text="Email Address:")
circuit_label.pack(fill='x', expand=True)
circuit_entry = Entry(w, textvariable=circuit)
circuit_entry.pack(fill='x', expand=True)
circuit_entry.focus()

# password
values_label = Label(w, text="Password:")
values_label.pack(fill='x', expand=True)
values_entry = Entry(w, textvariable=values, show="*")
values_entry.pack(fill='x', expand=True)
w.mainloop()