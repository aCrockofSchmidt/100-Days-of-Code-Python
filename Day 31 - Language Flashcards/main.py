from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


def update_word_dict():
    global word
    words_to_learn.remove(word)
    df = pd.DataFrame(words_to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():

    global word, words_to_learn, timer_reset
    word = random.choice(words_to_learn)
    window.after_cancel(timer_reset)
    language = "French"
    canvas.itemconfig(lang_text, text=language, fill="black")
    canvas.itemconfig(word_text, text=word[language], fill="black")
    canvas.itemconfig(canvas_image, image=fr_card)
    timer_reset = window.after(3000, answer_card)


def answer_card():
    global word
    language = "English"
    canvas.itemconfig(canvas_image, image=en_card)
    canvas.itemconfig(lang_text, text=language, fill="white")
    canvas.itemconfig(word_text, text=word[language], fill="white")


# --- IMPORT DATA ---

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    words_to_learn = data.to_dict(orient="records")

print(len(words_to_learn))

word = {}

# --- CREATE WINDOW ---

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer_reset = window.after(3000, answer_card)

# --- CREATE CANVAS ---

canvas = Canvas(width=800, height=526)
fr_card = PhotoImage(file="images/card_front.png")
en_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=fr_card)
lang_text = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# --- CREATE BUTTONS ---

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=update_word_dict)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()









# --- CREATE LABELS ---

# I initially added text to canvas using two labels. Instructor solution indicated create_text works better

# language_label = Label(text="Language", bg="white", font=("Arial", 40, "italic"))
# language_label.place(x=400, y=150, anchor=CENTER)
#
# word_label = Label(text="word", bg="white", font=("Arial", 60, "bold"))
# word_label.place(x=400, y=263, anchor=CENTER)

window.mainloop()
