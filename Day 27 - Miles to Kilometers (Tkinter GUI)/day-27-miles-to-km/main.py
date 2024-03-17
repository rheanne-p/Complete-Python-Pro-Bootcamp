from tkinter import *


# Constants
FONT = ("Arial", 24, "normal")


# Window
window = Tk()
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
window.title("Miles to Kilometers")


# Entry: Miles
miles_entry = Entry(width=20)
miles_entry.grid(column=1, row=0)


# Label: Miles
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=20)


# Label: is equal to
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)


# Label: converted km
converted_km_label = Label(text="0", font=FONT)
converted_km_label.grid(column=1, row=1)


# Label: Km
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


# Convert Measurements Function
def miles_to_km_convertor():
    km_conversion_arg = round(float(miles_entry.get()) * 1.609344, 3)
    converted_km_label.config(text=f"{km_conversion_arg}")


# Button: Calculate
calculate_button = Button(text="Calculate", command=miles_to_km_convertor)
calculate_button.grid(column=1, row=3)


# Window Close
window.mainloop()
