import tkinter as tk
from tkinter import messagebox

# Quiz data (you can add more)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Shakespeare", "Hemingway", "Tagore", "Tolstoy"],
        "answer": "Shakespeare"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Osmium", "Zinc"],
        "answer": "Oxygen"
    },
    {
        "question": "What is 9 x 9?",
        "options": ["81", "72", "99", "90"],
        "answer": "81"
    }
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")
        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            current_q = questions[self.q_index]
            self.question_label.config(text=f"Q{self.q_index+1}: {current_q['question']}")
            for i, option in enumerate(current_q['options']):
                self.option_buttons[i].config(text=option)
        else:
            self.show_result()

    def check_answer(self, selected_index):
        selected_option = self.option_buttons[selected_index].cget("text")
        correct_answer = questions[self.q_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.q_index += 1
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score} / {len(questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
