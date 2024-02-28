import math
import sympy as sp
from sklearn import datasets
olivetti_faces = datasets.fetch_olivetti_faces()
import tkinter as tk
from tkinter import messagebox
import random

def question1(number):
    # Ensuring input is between 1 and 100
    if number < 1 or number > 100:
        return False
    # Will return a true false statement if the number does not satisfy
    return (number + 1) % 6 == 0

def question2(x):
    # Checking if the denominator is zero
    if (3 * x - 7) == 0:
        return "Error: Division by zero is not allowed."
    
    # Calculating the numerator and denominator separately
    numerator = math.sqrt(x) + 3 * x**5
    denominator = 3 * x - 7
    
    # Calculating the value of the function
    result = numerator / denominator
    
    return result

def question3(a, b, c, d):
    x = sp.symbols('x')
    f = a*sp.sin(b*x) + c*sp.exp(d*x)

    # (a) Evaluate f(5)
    f_at_5 = f.subs(x, 5)

    # (b) Calculate (d^3)(f(x))/dx^3
    third_derivative = sp.diff(f, x, 3)
    third_derivative_at_x = third_derivative.subs(x, sp.Symbol('x'))

    # (c) Compute the integral between root 6 and 2*pi of f(x)dx
    integral = sp.integrate(f, (x, sp.sqrt(6), 2*sp.pi))

    return [f_at_5, third_derivative_at_x, integral]

class NumberGuessingGame:
    def __init__(self, master):
        # Initialize the game window
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.geometry("300x150")
        
        # Generate a random number for the player to guess
        self.random_number = random.randint(0, 100)
        
        # Initialize guess count
        self.guess_count = 0
        
        # Create GUI components
        self.label = tk.Label(master, text="Guess the number (0-100):")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        # Button to submit the guess
        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()
        
        # Button to reset the game
        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack()
        
        # Label to display hints or game messages
        self.hint_label = tk.Label(master, text="")
        self.hint_label.pack()
        
    def check_guess(self):
        # Retrieve user's guess
        guess = self.entry.get()
        try:
            guess = int(guess)  # Convert guess to an integer
            self.guess_count += 1  # Increment guess count
            
            # Compare guess with random number
            if guess == self.random_number:
                messagebox.showinfo("Congratulations!", "You guessed the number!")
                self.submit_button.config(state=tk.DISABLED)  # Disable submit button
                self.reset_button.config(state=tk.NORMAL)    # Enable reset button
            else:
                # Provide hint whether the guess is too high or too low
                hint = "Too high!" if guess > self.random_number else "Too low!"
                self.hint_label.config(text=f"Guess {self.guess_count}: {guess} - {hint}")
                
                # Check if user has made 6 guesses without guessing the correct number
                if self.guess_count == 6:
                    messagebox.showinfo("Game Over", f"You've made 6 guesses. The number was {self.random_number}, better luck next time lol.")
                    self.submit_button.config(state=tk.DISABLED)  # Disable submit button
                    self.reset_button.config(state=tk.NORMAL)    # Enable reset button
        except ValueError:
            # Handle exception if user enters invalid input (non-integer)
            messagebox.showerror("Error", "Please enter a valid integer.")
        
    def reset_game(self):
        # Reset the game
        self.random_number = random.randint(0, 100)  # Generate a new random number
        self.guess_count = 0  # Reset guess count
        self.entry.delete(0, tk.END)  # Clear entry field
        self.hint_label.config(text="")  # Clear hint label
        self.submit_button.config(state=tk.NORMAL)  # Enable submit button
        self.reset_button.config(state=tk.DISABLED)  # Disable reset button

def question4():
    # Create the main application window
    root = tk.Tk()
    
    # Instantiate the NumberGuessingGame class with the main application window as the master
    game = NumberGuessingGame(root)
    
    # Start the Tkinter event loop to run the application
    root.mainloop()
