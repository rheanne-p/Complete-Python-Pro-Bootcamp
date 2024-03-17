from tkinter import *

# Window Object
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label Object
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # pack places label onto screen, automatically centers
my_label["text"] = "New Text 1"
my_label.config(text="New Text")  # updates properties using config method


# Button Object

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()


# Entry Object
input = Entry(width=10)
new_text = input.pack()
print(input.get())


# Screen Listener
window.mainloop()

