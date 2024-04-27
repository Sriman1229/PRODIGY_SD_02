import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.root = tk.Tk()
        self.root.title("Guess The Number Game")

        self.label = tk.Label(self.root, text="Guess the number (between 1 and 100):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You've guessed the number {self.secret_number} correctly!\nIt took you {self.attempts} attempts to win the game.")
                self.root.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Too low!", "Too low! Try again.")
            else:
                messagebox.showinfo("Too high!", "Too high! Try again.")
        except ValueError:
            messagebox.showerror("Invalid input!", "Please enter a valid number.")

if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.root.mainloop()
