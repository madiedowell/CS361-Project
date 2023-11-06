from tkinter import *
from time import sleep
from PIL import Image, ImageTk
import random


messageBox = None  # Declare messageBox as a global variable

#Shuts down all windows
def clickExit():
    root.quit()

#Displays game instructions to user in seperate window
def showIntructions():

    root = Tk()

    root.title("How to Play")
    root.geometry("800x600")
    instructions_font = ("Helvetica", 25)

    text_widget = Text(root, font = instructions_font)
    text_widget.insert(INSERT, "How to Play Spin to Win\n\n Goal of the game: Be the first to solve the puzzle on the board. \n\n First Round: The player will take their turn before the CPU. In the first round, the player has to click Spin to Win. The players spin will display in the message box where they will be prompted to guess a consonant.\n\n")
    text_widget.insert(INSERT, "Guessing Right: If the player guesses correctly, they win the prize they spun from the wheel and they get to guess again. Guessing continues until player guesses incorectly or lands on BANKRUPT or\nLose a Turn.\n\n" )
    text_widget.insert(INSERT, "Landing on Bankrupt or Lose a Turn: If a player lands on Bankrupt, they lose all of the money they\nhad collected so far and their turn is over. If a player lands on Lose a Turn, their turn is over and their turn gets skipped in the next round.\n\n")
    text_widget.insert(INSERT, "Buying Vowels and Solving: Players are given the option to buy a vowel for $250 during their turn. If\nthe player guesses wrong, they lose $250 and if they guess right, they can keep it. Players are also\ngiven the option to solve the puzzle after the first round and after they have guessed a letter correctly or bought a vowel. If a player chooses to solve the puzzle and is wrong, they lose their turn")
    text_widget.pack() 

    root.mainloop()

#Game window
def newWindow():

    #Produces value randomly from list and prints it in the message box
    def showSpin():
        spins = ["$100", "$200", "$300", "$400", "$500", "$600", "$700", "$800", "$900", "$1,000", "BANKRUPT", "Lose a Turn"]
        random_spin = "Message Box\n" + random.choice(spins)
        messageBox.config(text= random_spin)

    root = Tk()

    root.title("Spin to Win")
    root.geometry("800x600")
    category_font = ("Noto Sans", 25)
    button_font = ("Helvetica", 25)
    letter_font = ("Helvetica", 17)
    underscore_font = ("Helvetica", 30)
    root.configure(bg="light blue")

    #Displays random word from list on game board. Represented with underscores.
    words = ["apple", "dog", "cat", "house", "ball", "car", "family", "friend"]
    random_word = random.choice(words)
    underscored_word = " _ " * len(random_word)

    #Game Board
    board = Label(root, 
        text= underscored_word, 
        width = 45, 
        height = 10, 
        relief="solid", 
        borderwidth=2,
        bg = "white",
        fg = "black",
        highlightthickness=2, 
        highlightbackground="yellow",
        font=underscore_font)
    
    board.grid(row=0, column=0, padx=10, pady=20)

    #Category
    category = Label(root, 
        text= "Category", 
        width = 25, 
        height = 1,
        relief="solid", 
        borderwidth=2,
        highlightthickness=2, 
        highlightbackground="blue",
        fg = "blue",
        bg = "light grey",
        font = category_font
        )
    
    category.grid(row=1, column=0, pady=10)

    #Spin to win button,
    spinToWin = Button(root,
            text = "Spin to Win",
            font = button_font,
            command = showSpin)
    
    spinToWin.grid(row=2, column=0, pady =5 , sticky="w")
    

    #Buy a Vowel button
    buyAVowel = Button(root,
            text = "Buy a vowel",
            font = button_font)
    
    buyAVowel.grid(row=3, column=0, pady =5 , sticky="w")

    #Solve button
    solve = Button(root,
            text = "Solve",
            font = button_font)
    
    solve.grid(row=4, column=0, pady = 5, sticky="w")

    #Message box for input/output
    global messageBox
    messageBox = Label(root, 
        text= "Message Box", 
        width = 30, 
        height = 10, 
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "nw")
    
    messageBox.grid(row= 5, column=0, pady = 5, padx = 5, sticky = "w")

    #Score box. Displays player and CPU scores. 
    scoreBox = Label(root, 
        text= "Score Box", 
        width = 30, 
        height = 10, 
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "nw")
    
    scoreBox.grid(row= 5, column=0, pady = 5, padx = 5, sticky = "e")

    #Shows available vowels
    vowels = Label(root,
        text = "vowels\n\n a   e   i   o   u",
        width = 20,
        height = 10,
        font = letter_font,
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "n")
    
    vowels.grid(row=0, column=1, padx= 20)

    #Shows available consonants
    consonants = Label(root,
        text = "consonants\n\n b   c   d   f   g   h   j   k\nl   m   n   p   q   r   s   t\n   v   w   x   y   z",
        width = 30,
        height = 10,
        font = letter_font, 
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "n")
    
    consonants.grid(row=0, column=2, padx = 20)

    root.mainloop()

#Welcome screen
root = Tk()

root.title("Spin to Win")
root.geometry("800x600")
welcome_font = ("Helvetica", 50)
button_font = ("Helvetica", 25)
root.configure(bg="lightblue")


image = Image.open("/Users/madiedowell/Documents/CS361/Assignment5/wheel2.jpeg")
resizeImage = image.resize((600, 500))
resizeImage.save("/Users/madiedowell/Documents/CS361/Assignment5/wheel2.jpeg")
photo = ImageTk.PhotoImage(image)

myLabel1 = Label(root, 
    text = "Welcome to Spin to Win!", 
    font = welcome_font,
    fg = "blue",
    bg = "yellow")

myLabel1.pack(pady = 20)

#New game button
myButton1 = Button(root, 
    text = "NEW GAME",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = newWindow)

myButton1.pack(pady = 5)

#How to play button
myButton2 = Button(root,
    text = "HOW TO PLAY",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = showIntructions)

myButton2.pack(pady = 5)

#Exit button
myButton3 = Button(root, 
    text = "EXIT",
    font = button_font,
    fg = "blue",
    bg = "yellow", 
    command = clickExit)

myButton3.pack(pady = 5)

#Wheel image
imageLabel = Label(root, image=photo,)
imageLabel.pack(pady = 20) 

root.mainloop()