from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
word_translation_pair = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    words_and_translations = pandas.DataFrame(data).to_dict("records")
    words_length = len(words_and_translations)
    known_words = 0


def next_card():
    global word_translation_pair, flip_timer, known_words
    canvas.itemconfig(points_display, text=f"{known_words}/{words_length}", fill="black")
    window.after_cancel(flip_timer)
    word_translation_pair = random.choice(words_and_translations)
    word = word_translation_pair[LANGUAGE]
    canvas.itemconfig(card_display, image=card_front_image)
    canvas.itemconfig(language_display, text=LANGUAGE, fill="black")
    canvas.itemconfig(french_word_display, text=word, fill="black")

    flip_timer = window.after(3000, func=flip_card)


def know_word():
    global known_words
    known_words += 1
    next_card()
    words_and_translations.remove(word_translation_pair)
    pandas.DataFrame(words_and_translations).to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    canvas.itemconfig(card_display, image=card_back_image)
    canvas.itemconfig(language_display, text="English", fill="white")
    canvas.itemconfig(french_word_display, text=word_translation_pair["English"], fill="white")
    canvas.itemconfig(points_display, text=f"{known_words}/{words_length}", fill="white")


# Window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Displays
flip_timer = window.after(3000, flip_card)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_display = canvas.create_image(400, 263, image=card_front_image)
language_display = canvas.create_text(400, 150, text=LANGUAGE, font=("Arial", 40, "italic"))
french_word_display = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
points_display = canvas.create_text(400, 450, text=f"{known_words}/{words_length}", font=("Arial", 30, "normal"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unknown_button_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_button_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0)

know_button_image = PhotoImage(file="images/right.png")
know_button = Button(image=know_button_image, highlightthickness=0, borderwidth=0, command=know_word)
know_button.grid(row=1, column=1)

next_card()
window.mainloop()
