from tkinter import *
from time import sleep
from PIL import Image, ImageTk
import random


messageBox = None  # Declare messageBox as a global variable


def clickExit():
    root.quit()

def showIntructions():
    root = Tk()

    button_font = ("Helvetica", 25)

    root.title("How to Play")
    root.geometry("800x600")
    instructions_font = ("Helvetica", 25)

    text_widget = Text(root, font = instructions_font)
    text_widget.insert(INSERT, "Insert instructions here")
    text_widget.pack() 

    myButton = Button(root, 
    text = "EXIT",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = clickExit)

    myButton.pack(pady = 5, anchor = "se") 

    root.mainloop()


def newWindow():

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

    words = ["apple", "dog", "cat", "house", "ball", "car", "family", "friend"]
    random_word = random.choice(words)
    underscored_word = " _ " * len(random_word)

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

    spinToWin = Button(root,
            text = "Spin to Win",
            font = button_font,
            command = showSpin)
    
    spinToWin.grid(row=2, column=0, pady =5 , sticky="w")
    

    buyAVowel = Button(root,
            text = "Buy a vowel",
            font = button_font)
    
    buyAVowel.grid(row=3, column=0, pady =5 , sticky="w")

    solve = Button(root,
            text = "Solve",
            font = button_font)
    
    solve.grid(row=4, column=0, pady = 5, sticky="w")

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
    
    messageBox.grid(row=0, column=1, padx= 20)

    scoreBox = Label(root, 
        text= "Score Box", 
        width = 30, 
        height = 10, 
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "nw")
    
    scoreBox.grid(row=0, column=2, padx = 20)

    vowels = Label(root,
        text = "vowels\n\n a   e   i   o   u",
        width = 30,
        height = 10,
        font = letter_font,
        relief="solid", 
        borderwidth=2, 
        highlightthickness=2, 
        highlightbackground="blue",
        anchor = "n")
    
    vowels.grid(row= 5, column=0, pady = 5, padx = 5, sticky = "w")

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
    
    consonants.grid(row= 5, column=0, pady = 5, padx = 5, sticky = "e")



    root.mainloop()


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

myButton1 = Button(root, 
    text = "NEW GAME",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = newWindow)

myButton1.pack(pady = 5)

myButton2 = Button(root,
    text = "HOW TO PLAY",
    font = button_font,
    fg = "blue",
    bg = "yellow",
    command = showIntructions)

myButton2.pack(pady = 5)

myButton3 = Button(root, 
    text = "EXIT",
    font = button_font,
    fg = "blue",
    bg = "yellow", 
    command = clickExit)

myButton3.pack(pady = 5)

imageLabel = Label(root, image=photo,)
imageLabel.pack(pady = 20) 






root.mainloop()