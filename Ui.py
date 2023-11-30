from tkinter import *
from time import sleep
from PIL import Image, ImageTk
import random
import ast


messageBox = None  # Declare messageBox as a global variable


#Shuts down all windows
def clickExit():
    exit = Toplevel(welcomeWindow)
    exit.title("Exit")
    welcomeWindow.geometry("600x400")

    exitLabel = Label(exit, text= "Are you sure you want to exit?")
    exitLabel.pack()
    
    yesButton = Button(exit, text = "Yes", command = welcomeWindow.quit)
    yesButton.pack()

    noButton = Button(exit, text = "No", command = exit.destroy)
    noButton.pack()

#Displays game instructions to user in seperate window
def showIntructions():

    instructions = Tk()

    instructions.title("How to Play")
    instructions.geometry("800x600")
    instructions_font = ("Helvetica", 25)

    text_widget = Text(instructions, font = instructions_font)
    text_widget.insert(INSERT, "How to Play Spin to Win\n\n Goal of the game: Be the first to solve the puzzle on the board. \n\n First Round: The player will take their turn before the CPU. In the first round, the player has to click Spin to Win. The players spin will display in the message box where they will be prompted to guess a consonant.\n\n")
    text_widget.insert(INSERT, "Guessing Right: If the player guesses correctly, they win the prize they spun from the wheel and they get to guess again. Guessing continues until player guesses incorectly or lands on BANKRUPT or\nLose a Turn.\n\n" )
    text_widget.insert(INSERT, "Landing on Bankrupt or Lose a Turn: If a player lands on Bankrupt, they lose all of the money they\nhad collected so far and their turn is over. If a player lands on Lose a Turn, their turn is over and their turn gets skipped in the next round.\n\n")
    text_widget.insert(INSERT, "Buying Vowels and Solving: Players are given the option to buy a vowel for $250 during their turn. If\nthe player guesses wrong, they lose $250 and if they guess right, they can keep it. Players are also\ngiven the option to solve the puzzle after the first round and after they have guessed a letter correctly or bought a vowel. If a player chooses to solve the puzzle and is wrong, they lose their turn\n\n")
    text_widget.insert(INSERT, "Risks and Rewards: Buying a vowel is a smart move if you have enough money. Every word contains a vowel and there are only so many to choose from. However, if you guess a vowel incorrectly, you will lose $250. If you think you know the puzzle, is it better to solve right away, or risk it and spin\nagain? The risk with spinning again is you may land on bankrupt and lose your turn.")
    text_widget.pack() 

    goBack = Button(instructions, text = "BACK", command = instructions.destroy)

    goBack.pack()

    instructions.mainloop()

#Starts microservice process
def showWordAndCategory():
    with open('SpinToWinInput.txt', 'w') as file1:
        file1.write('get')
        file1.close()


#Store word and category
def getWordAndCategory():
    with open('SpinToWinOutput.txt', 'r') as file2:
        response = file2.readline().strip()
        tuple_response = ast.literal_eval(response)
        
        category = tuple_response[0]
        word = tuple_response[1]
        underscored_word = " _ " * len(word)
        file2.close()
    return underscored_word, category, word

#Gets users guess and validates it
def getGuess(word):
    guessWindow = Tk()
    def storeGuess():
        guess = textentry.get()
        print(f"guess: {guess}")

        if guess == "" :
            print("Guess has not been made")
        elif guess in word:
            print("Guess is in word")
        else:
            print("Guess is not in word")

        #checkGuess()
        return guess
    guessWindow.geometry("100x50")
    textentry = Entry(guessWindow, width=10)
    textentry.grid(row=4, column=0, sticky='s') 
    submit_button = Button(guessWindow, text="Submit", command= storeGuess)
    submit_button.grid(row=5, column=0, sticky="n")  
    guessWindow.mainloop() 


 #Produces value randomly from list and prints it in the message box
def showSpin(word):
    spins = ["$100", "$200", "$300", "$400", "$500", "$600", "$700", "$800", "$900", "$1,000", "BANKRUPT", "Lose a Turn"]
    players_spin = random.choice(spins)
    random_spin = "Message Box\n" + players_spin + "\n\nGuess a consonant for " + players_spin + ": "
    messageBox.config(text= random_spin)
    getGuess(word)



#----------------------------------------------------------------------------------------------------------------------------------
    #tKinter window

#----------------------------------------------------------------------------------------------------------------------------------
#Game window
def newWindow():    
    gameWindow = Tk()

    gameWindow.title("Spin to Win")
    gameWindow.geometry("800x600")
    category_font = ("Noto Sans", 25)
    button_font = ("Helvetica", 25)
    letter_font = ("Helvetica", 17)
    underscore_font = ("Helvetica", 30)
    gameWindow.configure(bg="light blue")

    showWordAndCategory()

    underscored_word, category, word = getWordAndCategory()
    print(f"Underscored Word: {underscored_word}")
    print(f"Category: {category}")
    print(f"Word: {word}")


    #Game Board
    board = Label(gameWindow, 
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
    category = Label(gameWindow, 
        text= category, 
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
    spinToWin = Button(gameWindow,
            text = "Spin to Win",
            font = button_font,
            command = lambda: showSpin(word))
    
    spinToWin.grid(row=2, column=0, pady =5 , sticky="w")
    

    #Buy a Vowel button
    buyAVowel = Button(gameWindow,
            text = "Buy a vowel",
            font = button_font)
    
    buyAVowel.grid(row=3, column=0, pady =5 , sticky="w")

    #Solve button
    solve = Button(gameWindow,
            text = "Solve",
            font = button_font)
    
    solve.grid(row=4, column=0, pady = 5, sticky="w")

    #Message box for input/output
    global messageBox
    messageBox = Label(gameWindow, 
        text= "Message Box", 
        width = 30, 
        height = 10, 
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "nw")
    
    messageBox.grid(row= 5, column=0, pady = 5, padx = 5, sticky = "w")

    def displayTurnMessage():
        turn_message = "It's your turn first. Click Spin to Win!"
        current_text = messageBox.cget("text")  # Get the current text in messageBox
        updated_text = f"{current_text}\n\n{turn_message}"  # Add the turn message below the existing text
        messageBox.config(text=updated_text)  # Update the text of messageBox

    displayTurnMessage()  # Call the function to display the message in messageBox

    #Score box. Displays player and CPU scores. 
    scoreBox = Label(gameWindow, 
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
    vowels = Label(gameWindow,
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
    consonants = Label(gameWindow,
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
    
    gameWindow.mainloop()
    return word

#Welcome screen
welcomeWindow = Tk()

welcomeWindow.title("Spin to Win")
welcomeWindow.geometry("800x600")
welcome_font = ("Helvetica", 50)
button_font = ("Helvetica", 25)
welcomeWindow.configure(bg="lightblue")


image = Image.open("/Users/madiedowell/Documents/CS361/Assignment5/wheel2.jpeg")
resizeImage = image.resize((600, 500))
resizeImage.save("/Users/madiedowell/Documents/CS361/Assignment5/wheel2.jpeg")
photo = ImageTk.PhotoImage(image)

myLabel1 = Label(welcomeWindow, 
    text = "Welcome to Spin to Win!", 
    font = welcome_font,
    fg = "blue",
    bg = "yellow")

myLabel1.pack(pady = 20)

#New game button
myButton1 = Button(welcomeWindow, 
    text = "NEW GAME",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = newWindow)

myButton1.pack(pady = 5)

#How to play button
myButton2 = Button(welcomeWindow,
    text = "HOW TO PLAY",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = showIntructions)

myButton2.pack(pady = 5)

#Exit button
myButton3 = Button(welcomeWindow, 
    text = "EXIT",
    font = button_font,
    fg = "blue",
    bg = "yellow", 
    command = clickExit)

myButton3.pack(pady = 5)

#Wheel image
imageLabel = Label(welcomeWindow, image=photo,)
imageLabel.pack(pady = 20) 

welcomeWindow.mainloop()