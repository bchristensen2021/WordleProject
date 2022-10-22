# File: Wordle.py

# """
# This module is the starter file for the Wordle assignment.
# BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
# """

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS


def wordle():
    # Function that gets run when you click enter
    def enter_action(s):
        # Initialize the varaibles
        y = ""
        sWordGuess = ""
        x = 0
        iRow = gw.get_current_row()
        listTemp = []
        listTemp = lRandomWord.copy()

        # Get guess letters and concatenate them together into sWordGuess
        while x < 5:
            y = gw.get_square_letter(iRow, x)
            sWordGuess = sWordGuess.lower() + y
            x += 1

        # Convert the guessed word to lower case
        # Print the guessed word to the terminal for debugging
        sWordGuess = sWordGuess.lower()
        listWordGuess = list(sWordGuess)

        # Determine which message to display to the user.
        if sWordGuess in FIVE_LETTER_WORDS:
            gw.show_message("Word found.")
        else:
            gw.show_message("Word not found")

        # Assign the tile colors
        #GREEN
        for x in range(5):
            if listWordGuess[x] == listTemp[x]:
                gw.set_square_color(iRow, x, "#66BB66")
                #setting key color
                gw.set_key_color(listWordGuess[x].upper(), "#66BB66")
                listWordGuess[x] = "-"
                listTemp[x] = "-"
        #YELLOW
        for x in range(5):
            if listWordGuess[x] in listTemp and listWordGuess[x] != "-":
                gw.set_square_color(iRow, x, "#CCBB66")
                #setting key color
                gw.set_key_color(listWordGuess[x].upper(), "#CCBB66")
                listWordGuess[x] = "-"
                listTemp[x] = "-"
        #GRAY
        for x in range(5):
            if listWordGuess[x] != "-":
                gw.set_square_color(iRow, x, "#999999")
                #setting key color
                gw.set_key_color(listWordGuess[x].upper(), "#999999")

        # Move the current row to the next row
        gw.set_current_row(iRow + 1)

        # Iterate the iRow variable
        iRow += 1

        # Display a game over message if the guessed word matches the randomword
        if sRandomWord == sWordGuess:
            gw.show_message("You won! Game over")


# Startup code
#getting random word aka THE ANSWER

    sRandomWord = random.choice(FIVE_LETTER_WORDS)
    lRandomWord = list(sRandomWord)
    #use line 83 to have the word print to the console
    print(lRandomWord)

    # Display the wordle ui to the user
    gw = WordleGWindow()

    #printing word list to console
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()
