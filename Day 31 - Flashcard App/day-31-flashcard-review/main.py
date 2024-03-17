from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------ RANDOM WORD GENERATOR -------------------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
data_list = data.to_dict(orient="records")
current_entry = None


def next_word():
    global current_entry, flipping
    window.after_cancel(flipping)
    random_index = random.randint(0, len(data_list) - 1)
    current_entry = data_list[random_index]
    french_word = current_entry["French"]
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    flipping = window.after(3000, func=turn_card)


def turn_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_entry["English"], fill="white")


def correct():
    data_list.remove(current_entry)
    updated_dataframe = pandas.DataFrame(data_list)
    updated_dataframe.to_csv("./data/words_to_learn.csv")
    next_word()


# --------------------------- UI SETUP -----------------------------------------
window = Tk()
window.title("Flashcard - Review")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flipping = window.after(3000, func=turn_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)

language_text = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

next_word()

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=next_word)
wrong_button.config(highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, command=correct)
right_button.config(highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()
