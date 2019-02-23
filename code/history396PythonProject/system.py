# Matt Radke
# mmr174

import os
from tkinter import *
from tkinter import ttk


def buildMainMenu():

    mainPanel = Tk()

    mainPanel.title("Main Menu")


    # label title for the project.
    Label(mainPanel,  text = "Digital History 396 Graphical Textual Analysis Tool", font = ("Times New Roman", 16)).grid(row = 0)

    Label(mainPanel, text = "please drag a file into the entry:", font = ("Times New Roman", 12)).grid(row=1)
    Entry(mainPanel).grid(row=1, column = 1)




  #  ttk.Button(mainPanel, text="test").grid()

    return mainPanel



"""
Main panel,

"""

if __name__ == '__main__':

    mainPanel = buildMainMenu()

    mainPanel.mainloop()



