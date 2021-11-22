"""
Name:       Joseph Maiello
Date:       11/19/2021   
Program:    lotto.py 

*** Note: the file breezypythongui.py MUST be in the same directory as this file for the application to work.
ALSO NOTE: Please install the package PIL with the command: pip install pillow before using this with a non GIF image.
***
"""
import random
from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage
class MegaLotto(EasyFrame):
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Dream Big, Win Small", width = 800, height = 300, background = "DeepSkyBlue3", resizable = False)
        # Title label
        megaLogo = self.addLabel(text = "MEGA MILLIONS", row = 0, column = 0, columnspan = 6, background = "DeepSkyBlue3", foreground = "yellow", font = Font(family = "Georgia", size = 28), sticky = "NSEW")
        # Load the image and associate it with the megaLogo. 
        self.image = PhotoImage(file = "mega2.gif")
        megaLogo["image"] = self.image

        # Fields for the random numbers to appear
        self.rollField1 = self.addIntegerField(value = "Your 1st Number", row = 2, column = 0, sticky = "NSEW", state = "readonly")
        self.rollField2 = self.addIntegerField(value = "Your 2nd Number", row = 2, column = 1, sticky = "NSEW", state = "readonly")
        self.rollField3 = self.addIntegerField(value = "Your 3rd Number", row = 2, column = 2, sticky = "NSEW", state = "readonly")
        self.rollField4 = self.addIntegerField(value = "Your 4th Number", row = 2, column = 3, sticky = "NSEW", state = "readonly")
        self.rollField5 = self.addIntegerField(value = "Your 5th Number", row = 2, column = 4, sticky = "NSEW", state = "readonly")
        self.rollField6 = self.addIntegerField(value = "Mega 5x Number", row = 2, column = 5, sticky = "NSEW", state = "readonly")
        # Command button
        self.playButton = self.addButton(text = "Click", row = 3, column = 2, columnspan = 2, command = self.ballRoll)
        # Label for the output message
        self.outputLabel = self.addLabel(text = " ", row = 4, column = 0, columnspan = 6, sticky = "NSEW", background = "DeepSkyBlue3", foreground = "white", font = Font(family = "Georgia", size = 16))
    # Event handling Method
    def ballRoll(self):
        # Variables and constants
        roll1 = random.randint(0, 75)
        roll2 = random.randint(0, 75)
        roll3 = random.randint(0, 75)
        roll4 = random.randint(0, 75)
        roll5 = random.randint(0, 75)
        megaBall = random.randint(0, 25)
        # Determine the outcome of the game
        if roll1 == roll2 == roll3 == roll4 == roll5 == megaBall:
            result = "Congratulations, you have won the **MEGA MULTIPLIER** JACKPOT of $5,000,000!!!!"   
        elif roll1 == roll2 == roll3 == roll4 == roll5:
            result = "Congratulations, you have won the JACKPOT of $1,000,000!!!!"
        elif roll1 == roll2 or roll2 == roll3 or roll3 == roll4 or roll4 == roll5 or roll5 == roll1:
            result = "You have won a signed copy of District 9, Collectors Edition!!"            
        else:
            result = "Sorry, you are not a winner.  Please try again."
            
        # output phase
        self.rollField1.setNumber(roll1)
        self.rollField2.setNumber(roll2)
        self.rollField3.setNumber(roll3)
        self.rollField4.setNumber(roll4)
        self.rollField5.setNumber(roll5)
        self.rollField6.setNumber(megaBall)
        self.outputLabel["text"] = result

# definition of the main() function for program entry
def main():
    """Instantiates and pops up the window."""
    MegaLotto().mainloop()
# global call to trigger the main() function
if __name__ == "__main__":
    main()
