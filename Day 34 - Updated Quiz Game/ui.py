from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=300, width=300)
        self.question_text = self.canvas.create_text(
            150,
            150,
            font=FONT,
            width=275,
            fill=THEME_COLOR,
            text="Amazon acquired Twitch in August 2014 for $970 million dollars."
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0, command=self.correct_check)
        self.correct_button.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.wrong_check)
        self.wrong_button.grid(column=1, row=2)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

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
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_check(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_check(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




