from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

# Take random word from words and update flash card #

def next_card():
    global flip_timer
    global current_card
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(image, image=flash_card)
    canvas.itemconfig(top_text, text="French", fill="black")
    canvas.itemconfig(bottom_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card, current_card)

def flip_card(current_card):
    canvas.itemconfig(image, image=flash_back)
    canvas.itemconfig(top_text, text="English", fill="white")
    canvas.itemconfig(bottom_text, text=current_card["English"], fill="white")

def card_known():
    global current_card
    global data
    data = data[data["French"] != current_card["French"]]
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI Setup #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_card = []
flip_timer = window.after(3000, flip_card, current_card)



canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = PhotoImage(file="C:/Users/mikew/Downloads/flash-card-project-start/images/card_front.png")
flash_back = PhotoImage(file="C:/Users/mikew/Downloads/flash-card-project-start/images/card_back.png")
image = canvas.create_image(400, 263, image=flash_card)
canvas.grid(column=0, row=0, columnspan=2)
top_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
bottom_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="C:/Users/mikew/Downloads/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, relief=FLAT, bd=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="C:/Users/mikew/Downloads/flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, relief=FLAT, bd=0, command=card_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
