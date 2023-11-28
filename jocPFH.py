import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self, master):
        self.master=master
        self.master.title("Rock, Paper, Scissors")
        self.master.geometry("360x200")
        self.createWidgets()

        self.scorePlayer=0
        self.scoreComputer=0
        self.scoreTie=0
        self.updateScore()

    def createWidgets(self):
        self.label=tk.Label(self.master, text="Rock, Paper or Scissors?", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, columnspan=3, pady=(10,5))

        self.resultLabel=tk.Label(self.master, text="")
        self.resultLabel.grid(row=1, column=0, columnspan=3, pady=(10,10))

        self.scoreLabel = tk.Label(self.master, text="Player 0  Computer: 0  Tie: 0", font=("Helvetica", 12))
        self.scoreLabel.grid(row=3, column=0, columnspan=3, pady=(10, 5))
        
        self.rockBtn=tk.Button(self.master, text="Rock", font=("Helvetica", 12), width=10, command=lambda:self.playGame("Rock"))
        self.rockBtn.grid(row=2, column=0, padx=10, pady=(0,10))

        self.paperBtn=tk.Button(self.master, text="Paper", font=("Helvetica", 12), width=10, command=lambda:self.playGame("Paper"))
        self.paperBtn.grid(row=2, column=1, padx=10, pady=(0,10))

        self.scissorsBtn=tk.Button(self.master, text="Scissors",font=("Helvetica", 12), width=10, command=lambda:self.playGame("Scissors"))
        self.scissorsBtn.grid(row=2, column=2, padx=10,pady=(0,10))
    
    def playGame(self, userChoice):
        options=["Rock", "Paper", "Scissors"]
        computerChoice=random.choice(options)
        result=self.detWinner(userChoice, computerChoice)
        self.resultLabel.config(text= f"Computer chose {computerChoice}.\n {result}", font=("Helvetica", 12))
        self.updateScore()
    
    def detWinner(self, userChoice, computerChoice):
        if userChoice==computerChoice:
            self.resultLabel.config(text="It's a tie", fg="orange")
            self.scoreTie+=1
            return "It's a tie!"
        elif(
            (userChoice=="Rock" and computerChoice=="Scissors") or
            (userChoice=="Paper" and computerChoice=="Rock") or
            (userChoice=="Scissors" and computerChoice=="Paper") 
        ):
            self.resultLabel.config(text="You win!", fg="green")
            self.scorePlayer+=1
            return "You win!"
        else:
            self.resultLabel.config(text="Computer wins!", fg="red")
            self.scoreComputer+=1
            return "Computer wins!"
    
    def updateScore(self):
        scoreText=f"Player: {self.scorePlayer}  Computer: {self.scoreComputer}  Tie: {self.scoreTie}"
        self.scoreLabel.config(text=scoreText)

        if self.scorePlayer==10:
            messagebox.showinfo("Congrats!","You won the game!")
            self.master.destroy()

        elif self.scoreComputer==10:
            messagebox.showinfo("Game over!", "The computer won the game!")
            self.master.destroy()
    
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()