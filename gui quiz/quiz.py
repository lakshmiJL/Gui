import tkinter as tk
from tkinter import messagebox

class RiddleQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Riddle Quiz")

        self.questions = [
            ("What is the middle of Paris?", "R"),
            ("Which word is spelt wrong in every dictionary?", "Wrong"),
            ("What can you catch but not throw?", "Cold"),
            ("What animal can run the fastest- an elephant, squirrel or a mouse?", "Elephant"),
            ("I am an odd number, but if you take away just a single letter I become even. Can you guess my number?", "Seven"),
            ("I'm tall when I'm young, and I'm short when I'm old, what am I?", "Candle"),
            ("What is so fragile that saying its name breaks it?", "Silence"),
            ("What has four eyes but can't see?", "Mississippi"),
            ("Where can you find cities, towns, shops, and streets but no people?", "Map"),
            ("What has a neck but no head?", "Bottle")
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=300, justify="center")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, width=30)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.next_question_button = tk.Button(root, text="Next Question", command=self.next_question, state=tk.DISABLED)
        self.next_question_button.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        question, _ = self.questions[self.current_question]
        self.question_label.config(text=question)
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        _, answer = self.questions[self.current_question]
        user_answer = self.answer_entry.get().strip()

        if user_answer.lower() == answer.lower():
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer is: {answer}")

        self.score_label.config(text=f"Score: {self.score}")
        self.next_question_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.load_question()
            self.next_question_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}")
            self.root.destroy()

root = tk.Tk()
app = RiddleQuiz(root)
root.mainloop()
