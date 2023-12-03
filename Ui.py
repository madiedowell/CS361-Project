from tkinter import *
from time import sleep
from PIL import Image, ImageTk
import random
import ast


messageBox = None  # Declare messageBox as a global variable
scoreBox = None
board_label = None
underscored_word = None
players_spin = None
current_score = 1000


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

    return

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
    return

def updateBoard(new_text):
    global board_label
    if board_label:
        board_label.config(text=new_text)

#Starts microservice process
def showWordAndCategory():
    with open('SpinToWinInput.txt', 'w') as file1:
        file1.write('get')
        file1.close()
    return


#Store word and category
def getWordAndCategory():
    with open('SpinToWinOutput.txt', 'r+') as file2:
        sleep(2)
        response = file2.readline().strip()
        tuple_response = ast.literal_eval(response)
        
        category = tuple_response[0]
        word = tuple_response[1]
        underscored_word = " _ " * len(word)
        file2.truncate(0)
        file2.close()
    return underscored_word, category, word

def showScore(players_spin):
    global current_score
    global messageBox
    #current_score = 1000
    current_score = str(current_score)
    score = "Score Box\n\n$" + current_score

    current_score = int(current_score)

    if players_spin == "BANKRUPT":
        scoreBox.config(text=score)
        return
    
    elif current_score <= 0:
        loser_output = "Message Box\n\nYou lost!"
        messageBox.config(text= loser_output)

    scoreBox.config(text=score)
    return

def fillGameBoard(guess, word):
    global board_label
    global underscored_word

    if underscored_word == None:
        underscored_word = list("_ " * len(word))

    underscored_word = list(underscored_word)

    for index, letter in enumerate(word):
        if letter == guess:
            print(f"Letter '{guess}' found at index {index} in the word '{word}'")
            letter_position = index
            underscored_word[letter_position * 2] = guess

    underscored_word = ''.join(underscored_word)
    print(underscored_word)
    return underscored_word


def storeGuess(textentry, word, submit_button, players_spin):
    global current_score
    guess = textentry.get()
    print(f"guess: {guess}")

    vowels_list = ("a", "e", "i", "o", "u")

    if guess == "" :
        print("Guess has not been made")

    elif guess in vowels_list:
        guess_output = "Message Box\n\nTo guess a vowel, you must buy one for\n$200. See list of consonants and guess again."
        messageBox.config(text= guess_output)

        getGuess(word, players_spin)

    elif guess in word:
        print("Guess is in word")
        guess_output = "Message Box\n\nThere is a " + guess + ". You get $" + players_spin + ". \nSpin again!"
        messageBox.config(text= guess_output)
        fillGameBoard(guess, word)
        updateBoard(underscored_word)

        

        players_spin = int(players_spin)
        current_score = current_score + players_spin
        players_spin = str(players_spin)

        showScore(players_spin)

        noSpace_underscored_word = underscored_word.replace(" ", "")

        if noSpace_underscored_word == word:
            correct_guess = "Message Box\n\nYou got it! Congrats winner!"
            messageBox.config(text= correct_guess)
            return

    else:
        print("Guess is not in word")
        guess_output = "Message Box\n\nThere is no " + guess + ". Spin again."
        messageBox.config(text= guess_output)

        players_spin = int(players_spin)
        current_score = int(current_score) - int(players_spin/2)
        if current_score < 0:
            current_score = 0
        players_spin = str(players_spin)

        showScore(players_spin)
    
    #disable submit button after clicked once
    submit_button.config(state=DISABLED)

    #guessWindow.destroy()
    #checkGuess()
    return 

#Gets users guess and validates it
def getGuess(word, players_spin):

    guessWindow = Tk()  
    guessWindow.title("Enter Your Guess")
    #guessWindow.geometry("100x50")

    textentry = Entry(guessWindow, width=10)
    #textentry.grid(row=4, column=0, sticky='s') 
    textentry.pack()
    submit_button = Button(guessWindow, text="Submit", command= lambda: storeGuess(textentry, word, submit_button, players_spin))
    #submit_button.grid(row=5, column=0, sticky="n")  
    submit_button.pack()
      
    guessWindow.mainloop() 
    return submit_button


 #Produces value randomly from list and prints it in the message box
def showSpin(spinToWin, word):
    global underscored_word
    global current_score

    spins = ["100", "200", "300", "400", "500", "600", "700", "800", "900", "1000", "BANKRUPT"]
    players_spin = random.choice(spins)

    if underscored_word != None:
        noSpace_underscored_word = underscored_word.replace(" ", "")

        if noSpace_underscored_word == word:
            spinToWin.config(state=DISABLED)
            return


        elif players_spin == spins[10]:
            print("Bankrupt")
            random_spin = "Message Box\n" + players_spin + "\n\nUh Oh! You went bankrupt."
            messageBox.config(text= random_spin)
        else:
            print("Value")
            random_spin = "Message Box\n$" + players_spin + "\n\nGuess a consonant for " + players_spin + ": "
            messageBox.config(text= random_spin)
            getGuess(word, players_spin)
    else:
        if players_spin == spins[10]:
            print("Bankrupt")
            random_spin = "Message Box\n" + players_spin + "\n\nUh Oh! You went bankrupt.\nYou must solve the puzzle now."
            messageBox.config(text= random_spin)

            current_score = 0
            showScore(players_spin)

            solvePuzzle(word)

        else:
            print("Value")
            random_spin = "Message Box\n$" + players_spin + "\n\nGuess a consonant for " + players_spin + ": "
            messageBox.config(text= random_spin)
            getGuess(word, players_spin)

    return 

def checkVowel(vowel_entry, word, submit_button):
    global underscored_word
    global current_score
    global messageBox

    vowel_guess = vowel_entry.get()
    vowels_list = ("a", "e", "i", "o", "u")

    if vowel_guess not in vowels_list:
        wrong_guess_output = "Message Box\n\nThat is not a vowel.\nSee list of vowels and try again."
        messageBox.config(text= wrong_guess_output)
        getVowel(word)

    elif vowel_guess in word: 
        guess_output = "Message Box\n\nThere is a " + str(vowel_guess) + ". You get $300\nSpin again!"
        messageBox.config(text= guess_output)
        fillGameBoard(vowel_guess, word)
        updateBoard(underscored_word)

        submit_button.config(state=DISABLED)

        current_score = current_score + 300
        showScore(players_spin)

    else:
        guess_output = "Message Box\n\nThere is no " + str(vowel_guess) + "."
        messageBox.config(text= guess_output)

        submit_button.config(state=DISABLED)

        current_score = current_score + 300
        showScore(players_spin)


def getVowel(word):
    global current_score
    global messageBox

    vowel_message = "Message Box\n\n-$200\nGuess a vowel."
    messageBox.config(text= vowel_message)

    current_score = current_score - 200
    showScore(players_spin)

    vowelWindow = Tk()

    vowel_entry = Entry(vowelWindow, width=10)

    vowel_entry.pack()
    submit_button = Button(vowelWindow, text="Submit", command = lambda: checkVowel(vowel_entry, word, submit_button))
    submit_button.pack()

    vowelWindow.mainloop()


def checkSolve(solve_entry, word, submit_button):
    global messageBox
    
    solve_guess = solve_entry.get()

    print(f"word: {word}")
    print(f"solve guess: {solve_guess}")

    if solve_guess == word:
        print("That is correct")
        correct_guess = "Message Box\n\n That is correct! Congrats you win!"
        messageBox.config(text= correct_guess)

        submit_button.config(state=DISABLED)

    else:
        print("That is incorrect")
        incorrect_guess = "Message Box\n\n That is incorrect. Sorry you lose."
        messageBox.config(text= incorrect_guess)

        submit_button.config(state=DISABLED)


def solvePuzzle(word):
    solveWindow = Tk()

    solve_entry = Entry(solveWindow, width=10)

    solve_entry.pack()
    submit_button = Button(solveWindow, text="Submit", command = lambda: checkSolve(solve_entry, word, submit_button))
    submit_button.pack()

    solveWindow.mainloop()


#----------------------------------------------------------------------------------------------------------------------------------
    #tKinter window

#----------------------------------------------------------------------------------------------------------------------------------
#Game window
def newWindow():    
    gameWindow = Tk()

    global board_label
    #welcomeWindow.destroy()

    gameWindow.title("Spin to Win")
    gameWindow.geometry("800x600")
    category_font = ("Noto Sans", 25)
    button_font = ("Helvetica", 25)
    letter_font = ("Helvetica", 17)
    underscore_font = ("Helvetica", 30)
    gameWindow.configure(bg="light blue")

    showWordAndCategory()


    #Game Board
    board_label = Label(gameWindow, 
        #text= underscored_word, 
        width = 45, 
        height = 10, 
        relief="solid", 
        borderwidth=2,
        bg = "white",
        fg = "black",
        highlightthickness=2, 
        highlightbackground="yellow",
        font=underscore_font)
    
    board_label.grid(row=0, column=0, padx=10, pady=20)

    underscored_word, category, word = getWordAndCategory()
    updateBoard(underscored_word)
    print(f"Underscored Word: {underscored_word}")
    print(f"Category: {category}")
    print(f"Word: {word}")

    

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
            command = lambda: showSpin(spinToWin, word))
    
    spinToWin.grid(row=2, column=0, pady =5 , sticky="w")
    

    #Buy a Vowel button
    buyAVowel = Button(gameWindow,
            text = "Buy a vowel",
            font = button_font,
            command = lambda: getVowel(word))
    
    buyAVowel.grid(row=3, column=0, pady =5 , sticky="w")

    #Solve button
    solve = Button(gameWindow,
            text = "Solve",
            font = button_font,
            command = (lambda: solvePuzzle(word)))
    
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
        turn_message = "Click Spin to Win!"
        current_text = messageBox.cget("text")  # Get the current text in messageBox
        updated_text = f"{current_text}\n\n{turn_message}"  # Add the turn message below the existing text
        messageBox.config(text=updated_text)  # Update the text of messageBox

    displayTurnMessage()  # Call the function to display the message in messageBox

    #Score box. Displays player and CPU scores. 
    global scoreBox
    scoreBox = Label(gameWindow, 
        text= "Score Box\n\n$1000", 
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