from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Labels
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 20, "normal"))
        self.score_label.grid(row=0, column=1)

        # self.question_label = Label(text="Question goes here", height=10, width=20, font=FONT, bg="white")
        # self.question_label.grid(row=1, column=0, columnspan=2, pady=30)
        #

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question goes here", fill=THEME_COLOR,
                                                     font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, borderwidth=0, command=self.is_correct)
        self.true_button.grid(row=2, column=1)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, borderwidth=0, command=self.is_wrong)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
