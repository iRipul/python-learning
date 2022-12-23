from tkinter import *


def miles_to_km(miles):
    output_label.config(text=round(float(miles) * 1.609))


window = Tk()
window.config(padx=20, pady=20)
window.title("Miles to KM converter")
window.minsize(width=300, height=100)
# 4 labels , 1 input , 1 button
Label(text="Miles").grid(row=0, column=2)
Label(text="is equals to").grid(row=1, column=0)
output_label = Label(text="")
output_label.grid(row=1, column=1)
Label(text="Km").grid(row=1, column=2)
input_box = Entry(width=10)
input_box.grid(row=0, column=1)
Button(text="Calculate", command=lambda: miles_to_km(input_box.get())).grid(row=2, column=1)
window.mainloop()
