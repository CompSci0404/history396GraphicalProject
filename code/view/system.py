# Matt Radke
# mmr174

import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk


#class RaisePage(tk.Frame):



"""
This file runs the entire GUI system for my project. It all starts with the the start page class
this class begins the system, and aquires information from the user. This file is setup in different classes.
Each class is its own seperate page. 
"""

class startPage(tk.Frame):

    mainMenu = None     #mainMenu, the root for this class, it is the parnet panel, that holds all the content within side of it.
    path = None         # data path that is acquired through interacting with system.

    """
    init(mainMenu):
    
    mainMenu:   The root, or parent GUI object.
    
    this method builds the starting page that is seen when the program first starts. 
    """
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)




        # ---[[creating the main panel ]] --- #

        self.mainMenu = args[0]
        self.mainMenu.title("Digital History 396 Graphical Textual Analysis Tool")

    #---[[label, instructions gives the user a instruction to follow]]---#
        self.instruction = Label(self.mainMenu, text="find the directory in which you want to conduct stylometric analysis!")
        self.instruction.grid(row = 1, column = 1)

    #---[[this button has a action listener attached that calls the windows explorer to find a directory folder.]]---#
        self.dirButton = Button(self.mainMenu, text = "search Directory", command = lambda : self.buildDirWin(self.mainMenu)) # lambda is kind of weird, this allows me to add in custom methods from what I understand.
        self.dirButton.grid(row = 4, column = 1 )

        #---[[this button activates once the user has aquired a directory to find DATA.]]---#
        self.nextButton = Button(self.mainMenu, text = "Next Page", state=DISABLED, command = lambda : self.nextButtonPressed(self.mainMenu))
        self.nextButton.grid(row = 4, column = 2)

    #---[[directoryPath, a label which contains the selected data path that the user has found.]]---#
        self.directoryPath = Label(self.mainMenu, text= " ")
        self.directoryPath.grid(row= 3, column = 1)

    #---[[Quit button, exits the system.]]---#
        self.Quit_Button = Button(self.mainMenu, text = "Exit", command = self.mainMenu.quit)
        self.Quit_Button.grid(row = 4, column = 4)



    """
    buildDirWin(MainMenu): 
    
    mainMenu: is the root, or parent page, use this to access TK()
    
    method opens up file explorer on OS system, allows users to find the directory with the data that they want to use.
    Once the directory is selected, the path to that directory is returned from the file explorer window. Stores the 
    dirctory path into the instance variable directory. 
    
    """

    def buildDirWin(self, mainMenu):

        mainMenu.directory = filedialog.askdirectory( title= "search for directory!")

        self.path = mainMenu.directory                                   # once we find the correct data path, lets save it.
        self.directoryPath.config(text = "SELECTED PATH: " + self.path)  # show the selected data path.
        self.nextButton.config(state=NORMAL)                             # activate NEXT button, to procceed to next page.


    def nextButtonPressed(self, mainMenu):

        mainMenu.withdraw()
        newFrame = buildAuthor(mainMenu, self.path)





class buildAuthor(tk.Toplevel):
    root = None
    dataPath = None

    def __init__(self, root, dataPath):
        tk.Toplevel.__init__(self)

        self.root = root
        self.dataPath = dataPath
        

        self.label6 = Label(self, text = "hoi")
        self.label6.pack(side="top", fill = "both", expand=True)






if __name__ == '__main__':

    root = tk.Tk()

    my_gui = startPage(root)

    root.mainloop()

