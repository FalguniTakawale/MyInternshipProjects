import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(3):
            button = tk.Button(master, text="", command=lambda i=i: self.check_answer(i))
            button.pack(fill=tk.X)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question, options, correct_answer = self.questions[self.current_question]
            self.question_label.config(text=question)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
            self.correct_answer = correct_answer
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
            self.master.destroy()

    def check_answer(self, selected_index):
        selected_option = self.questions[self.current_question][1][selected_index]
        if selected_option == self.correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Your answer is incorrect. The correct answer is: {self.correct_answer}")
        self.current_question += 1
        self.next_question()

# Define the questions, options, and correct answers
questions = [
    ("What is the capital of France?", ["Paris", "Berlin", "London"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Mars", "Jupiter", "Saturn"], "Mars"),
    ("What is the largest mammal?", ["Elephant", "Blue whale", "Giraffe"], "Blue whale")
]

# Create the Tkinter window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

# Create an instance of the QuizApp
app = QuizApp(root, questions)

# Run the Tkinter event loop
root.mainloop()
