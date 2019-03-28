# Matt Radke
# mmr174

import os
from tkinter import *
from tkinter import ttk





"""
buildMainMenu(): 
param: None
Builds the main menu needed for, the project. 
When the system frist starts this is what is built and displayed to the user.
Main menu will quickly build  the basic gui application needed for the textual anaylsis.
return: Returns a reference to the Main Panel. 
"""
def buildMainMenu():
    print("hoi")
    mainPanel = Tk()

    mainPanel.title("Main Menu")


    # label title for the project.
    Label(mainPanel,  text = "Digital History 396 Graphical Textual Analysis Tool", font = ("Times New Roman", 16)).grid(row = 0)

    Label(mainPanel, text = "please drag a file into the entry:", font = ("Times New Roman", 12)).grid(row=1)
    FilePath = Entry(mainPanel).grid(row=1, column = 1)

    Button(mainPanel, text = "Quit", font = ("Times New Roman", 12), command = mainPanel.quit).grid(row = 2)
   # FilePath.get()


  #  ttk.Button(mainPanel, text="test").grid()

    return mainPanel



"""
Main panel,
"""

if __name__ == '__main__':

    mainPanel = buildMainMenu()

    mainPanel.mainloop()


