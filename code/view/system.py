# Matt Radke
# mmr174
#---[[Controller package I built, used to interact with only the data in the model. The view intakes data tells model it has data, controller deals with data and updates Model.]]---#
from controller import controller

#---[[tkinter imports:]]---#
from tkinter import filedialog
from tkinter import *
import tkinter as tk

#---[[String manipulation import:]]---#
import re

"""
This file runs the entire GUI system for my project. It all starts with the the start page class
this class begins the system, and aquires information from the user. This file is setup in different classes.
Each class is its own seperate page. 
"""

FONT = ("Times New Roman", 12)  # font that is wanted to be used in the system, it is in a variable, so I can easliy change it once and it changes everything.

class startPage(tk.Frame):

    mainMenu = None     #mainMenu, the root for this class, it is the parnet panel, that holds all the content within side of it.
    path = None         # data path that is acquired through interacting with system.

    """
    init(mainMenu):
    
    mainMenu:   The root, or parent GUI object.
    
    this method builds the starting page that is seen when the program first starts. 
    """
    def __init__(self, *args, **kwargs):                                    # this allows me to have multiply arguments, interesting if I ever want to add more or expand on this project.
        tk.Frame.__init__(self, *args, **kwargs)




        # ---[[creating the main panel ]] --- #

        self.mainMenu = args[0]

        self.mainMenu.title("Digital History 396 Graphical Textual Analysis Tool")

    #---[[label, instructions gives the user a instruction to follow]]---#
        self.instruction = Label(self.mainMenu, text="find the directory in which you want to conduct stylometric analysis!", font = FONT)
        self.instruction.grid(row = 1, column = 1)

    #---[[this button has a action listener attached that calls the windows explorer to find a directory folder.]]---#
        self.dirButton = Button(self.mainMenu, text = "search Directory", font=FONT, command = lambda : self.buildDirWin(self.mainMenu)) # lambda is kind of weird, this allows me to add in custom methods from what I understand.
        self.dirButton.grid(row = 4, column = 1 )

        #---[[this button activates once the user has aquired a directory to find DATA.]]---#
        self.nextButton = Button(self.mainMenu, text = "Next Page", font=FONT, state=DISABLED, command = lambda : self.nextButtonPressed(self.mainMenu))
        self.nextButton.grid(row = 4, column = 2)

    #---[[directoryPath, a label which contains the selected data path that the user has found.]]---#
        self.directoryPath = Label(self.mainMenu, text= " ", font = FONT)
        self.directoryPath.grid(row= 3, column = 1)

    #---[[Quit button, exits the system.]]---#
        self.Quit_Button = Button(self.mainMenu, text = "Exit", font = FONT, command = self.mainMenu.quit)
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




"""

Second page that the user encounters! This page will get the user to input the data required for the author to help
build the models data.

"""
class buildAuthor(tk.Toplevel):
    root = None
    dataPath = None

    def __init__(self, root, dataPath):
        tk.Toplevel.__init__(self)

        self.root = root        # store the root, and the data path from last window.
        self.dataPath = dataPath



        #self.geometry("100x100")
        self.Instruction = Label(self, text = "Input number of authors that will be searched:", font=FONT)  # provide instruction on what to do!
        self.Instruction.grid(row= 1, column = 1)

        self.numAuthor = Entry(self)                                                                        # a entry to input how many authors are within the data that is wanted to be calculated.
        self.numAuthor.grid(row = 1, column = 2)

        self.backButton = Button(self,text = "back", font=FONT,command = lambda : self.backToStart())       # head back to pervious page.
        self.backButton.grid(row = 3, column= 1)

        self.submitButton = Button(self, text = "Submit", font=FONT, command = lambda:self.submitEntry())   # submit number of authors.
        self.submitButton.grid(row = 3, column = 2)

        self.errorLabel = Label(self, text="", font=FONT )
        self.errorLabel.grid(row = 4, column = 2)


    """
    backToStart():
    Action listener, when back button is clicked it will do this method worth of code. Basically it will
    head back to the start of the GUI system, incase someone screwed up on directory or just wants to go back.
    
    """
    def backToStart(self):

        self.destroy()

        root.update()
        root.deiconify()


    """
    submitEntry():
    submits the total number of authors, that have been requested by the user. Once that number has been acquried
    it will build a total number of slots for the user to enter data into. 
    """
    def submitEntry(self):



        if(len(self.numAuthor.get()) == 0):                         # check to see if the entry is not null.
            self.errorLabel.config(text = "Please input a value!")
        else:
            self.errorLabel.config(text = "")                       # else, time to get to work.

            counter = 0
            lastRow = 4                                             # I just want to position the new entrys, and text under neath the last row, I will just keep adding rows.
            numberAuthors = int(self.numAuthor.get())               # get the number of authors from the input text field.


                                                                    # all the new GUI parts that we are going to add, we will store them within these dictionaries.
            dictionaryOfAuthorLabels = {}
            dictionaryOfAuthorEntrys = {}

            dictionaryOfWorksLabels = {}
            dictionaryOfWorksEntrys = {}

            while(counter <  numberAuthors):                                                                            # count throw how many authors we want, that is how many pieces we put into the FRAME.

                                                                                                                        # Basically I created a variable called authIn0......N, then I said for this variable store in a GUI Object.

                                                                                                                        # store labels, for the authors NAME, basically this is just a instruction, so user knows what to put.
                dictionaryOfAuthorLabels["authIn"+str(counter)] = Label(self, text="Input Authors Name:", font= FONT)
                dictionaryOfAuthorLabels["authIn"+str(counter)].grid(row = lastRow + 1, column = 1)                     # neat little Idea I had, just keep adding onto the row to add each label.

                # A dictionary entry, stores the entry field for the corriersponding label above
                dictionaryOfAuthorEntrys["authIn"+str(counter)] = Entry(self)
                dictionaryOfAuthorEntrys["authIn"+str(counter)].grid(row = lastRow + 1, column = 2)                     # the rest of these dictionaries do the same thing, they build a number of different GUI pieces and keep track of them.

                dictionaryOfWorksLabels["authIn" + str(counter)] = Label(self,text="Input file numbers that belong to this author",font=FONT)
                dictionaryOfWorksLabels["authIn" + str(counter)].grid(row=lastRow + 1, column=3)

                dictionaryOfWorksEntrys["authIn" + str(counter)] = Entry(self)
                dictionaryOfWorksEntrys["authIn" + str(counter)].grid(row = lastRow + 1, column = 4)


                lastRow += 1
                counter += 1

            # create a new button, this button will progress to the next page.
            self.doneButton = Button(self, text="submit data:", font=FONT, command = lambda : self.FrameDone( dictionaryOfAuthorEntrys, dictionaryOfWorksEntrys))
            self.doneButton.grid(row=lastRow + 1, column = 5)

            # move the back button down to bottom of this GUI page.
            self.backButton.grid_configure(row = lastRow +1 , column = 1)
            self.submitButton.destroy() # destory the submit button because data has been recorded.

    """
    FrameDone(dict1, dict2):
        dict1: this is all gui entries for Authors, gains information from each author.
        dict2: all the entries for file numbers that belong to a certain author.
        
        builds the entry data from the GUI panel into use able data for the MODEL classes. 
        
    """

    def FrameDone(self, dictionaryOfEntrys, dicOfWorkEnt):

        dictionaryForModel = {} # the final dictionary that will be sent to the model.
        listOfStrNum = []       # lists used to aquire all the numbers in the input entry section.
        listOfNumbers = []

        # first lets do a little check!
        counter = 0
        dataFilled = True


        while(counter < len(dictionaryOfEntrys)):   # first lets do a check to see if all entries have been filled, if one of them is equal to 0 then we have nothing in this entry.

            if(dictionaryOfEntrys["authIn"+ str(counter)].get() == 0 or dicOfWorkEnt["authIn" + str(counter)].get() == 0):

                self.errorLabel.config(text = "please fill in all entry items in the Panel!")
                dataFilled = False

            counter += 1

        if(dataFilled):                                     # if the data checks out, then we are green to proceed:

            self.errorLabel.config(text = "")


            for key, value in dictionaryOfEntrys.items():   # count through all the content

                Author = str(dictionaryOfEntrys[key].get())# get the authors.

                numbers = str(dicOfWorkEnt[key].get())      # get all the numbers per each entry.

                listOfStrNum = re.findall('\d+', numbers)   # store them in a list.

                k = 0

                while(k < len(listOfStrNum)):

                    listOfNumbers.append(int(listOfStrNum[k]))  # convert string numbers into Integer numbers.

                    k+=1

                print(listOfNumbers)

                dictionaryForModel[Author] = set(listOfNumbers) # store all the data into dictionary for model.


                listOfStrNum.clear()
                listOfNumbers.clear()


            print("After doing all calculations this is what we got:\n",dictionaryForModel)

            con = controller.controller()                   # tell model, we got some data.


            con.authorBuild(dictionaryForModel)

            self.withdraw()                                 # move to the next window page.
            newFrame = testingPage(con)



class testingPage(tk.Toplevel):

    con = None

    def __init__(self, controller):
        tk.Toplevel.__init__(self)

        self.con = controller
        self.label = Label(self, text = "made it!")
        self.label.pack()






if __name__ == '__main__':

    root = tk.Tk()

    my_gui = startPage(root)

    root.mainloop()

