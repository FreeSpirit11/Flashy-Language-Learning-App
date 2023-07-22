#watch lecture 31 to make csv file of most frequently used words of language you want to learn.
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
LEARNING_LANGUAGE="French"
PRIMARY_LANGUAGE="English"
card_title_FONT=("Ariel", 40, "italic")
LANGUAGE_FONT=("Ariel", 60, "bold")

#displaying next word
def next_card():
    global current_card, flip_timer, to_learn

    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        current_card = random.choice(to_learn)
    else:
        to_learn = data.to_dict(orient="records")
        current_card = random.choice(to_learn)

    window.after_cancel(flip_timer)
    canvas.itemconfig(flash_card, image=card_front)
    canvas.itemconfig(card_title, text=LEARNING_LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[LEARNING_LANGUAGE], fill="black")
    flip_timer=window.after(3000, func=flip_card)

#flip card
def flip_card():

    canvas.itemconfig(flash_card, image=card_back)
    canvas.itemconfig(card_title, text=PRIMARY_LANGUAGE, fill="white")
    canvas.itemconfig(card_word, text=current_card[PRIMARY_LANGUAGE], fill="white")

def right_click():
    to_learn.remove(current_card)
    new_data=pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#getting card_words from csv file
data = pandas.read_csv("./data/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card = {}

flip_timer = window.after(3000, func=flip_card)

card_front=PhotoImage(file="./images/card_front.png")
card_back=PhotoImage(file="./images/card_back.png")
right=PhotoImage(file="./images/right.png")
wrong=PhotoImage(file="./images/wrong.png")

canvas=Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#front_card_creation
flash_card=canvas.create_image(400, 263, image=card_front)
card_title=canvas.create_text(400, 150,  font=card_title_FONT)
card_word = canvas.create_text(400, 263, font=LANGUAGE_FONT)

#Buttons
right_button=Button(image=right, highlightthickness=0, command=right_click)
right_button.grid(row=1, column=1)
wrong_button=Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()

