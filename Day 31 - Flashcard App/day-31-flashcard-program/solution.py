from tkinter import *
import pandas
import random


# ---------------------------- NEXT CARD ------------------------------- #
current_word = {}
english_word = ""
try:
    contents = pandas.read_csv("./data/words_to_learn_sol.csv")
except FileNotFoundError:
    contents = pandas.read_csv("./data/indo_words.csv")
finally:
    contents_list = contents.to_dict(orient="records")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(contents_list)
    canvas.itemconfig(language_text, text="Indonesian", fill="black")
    canvas.itemconfig(vocab_text, text=current_word["Indonesian"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    global current_word, contents_list
    contents_list.remove(current_word)
    contents_dataframe = pandas.DataFrame(contents_list)
    contents_dataframe.to_csv("./data/words_to_learn_sol.csv")
    next_card()


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(vocab_text, text=current_word["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
VOCAB_FONT = ("Arial", 60, "bold")

window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")  # in def will lose reference
canvas_img = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, font=LANGUAGE_FONT)
vocab_text = canvas.create_text(400, 263, font=VOCAB_FONT)
canvas.grid(column=0, row=0, columnspan=2)

x_img = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_img, command=next_card, highlightthickness=0)
x_button.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
check_button = Button(image=check_img, command=is_known, highlightthickness=0)
check_button.grid(column=1, row=1)

next_card()

window.mainloop()
