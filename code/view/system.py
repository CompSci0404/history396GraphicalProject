

"""
Matt Radke: Historical 396 Digital History Textual anaylsis project

This system I developed was inspired and built upon off the following programming Historian lesson:

https://programminghistorian.org/en/lessons/introduction-to-stylometry-with-python

The model tests used for Mendhall testing, Kilgariff and Zscores tests have been taken and adapted to fit this GUI system.
"""

#---[[Controller package I built, used to interact with only the data in the model. The view intakes data tells model it has data, controller deals with data and updates Model.]]---#
from controller import controller

#---[[tkinter imports:]]---#
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import messagebox


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
        self.mainMenu.protocol( "WM_DELETE_WINDOW", lambda :self.closing(self.mainMenu))
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


    def closing(self, mainMenu):

        if(messagebox.askokcancel("Quit", "do you want to quit?")):

            mainMenu.destroy()

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

        self.protocol("WM_DELETE_WINDOW", lambda: self.closing())


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


    def closing(self):

        if (messagebox.askokcancel("Quit", "do you want to quit?")):
            self.root.destroy()
            #self.destroy()

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


            self.notice = Label(self, text= "*Notice* if you want to run the kilgariff test there needs to be a 'Disputed' author entered into the following entry sections. This allows the program to determine author ship of a work. ")
            self.notice.grid(row = 5, column = 1)

            counter = 0
            lastRow = 5                                             # I just want to position the new entrys, and text under neath the last row, I will just keep adding rows.
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


            con.authorBuild(dictionaryForModel, self.dataPath)

            self.withdraw()                                 # move to the next window page.
            newFrame = testingPage(con, self.root)


"""
Testing page(): 

this class is the page that allows the user to conduct all there testing it offers three tests

1. the first test is the Mendenhall test quite simple, just press the button and it displays all the authors and number words they have written on a graph.
2. The second test is the Kilgariff test, which can read Disputed files and calculate a CHI-square  stat to determine the likeliness of a author being the author of the Disputed test.
3. the Third and final test will combine all the writings and find the most common word in the entire collection.

"""

class testingPage(tk.Toplevel):

    con = None                  # a reference to the controller class.
    root = None
    authorSelectedForKilg = []
    lastRow = 0

    def __init__(self, controller, root):
        tk.Toplevel.__init__(self)

        # the Mendhall test, layed out here, just a button to press very nice!
        self.con = controller
        self.root = root

        self.protocol("WM_DELETE_WINDOW", lambda: self.closing())


        self.label = Label(self, text = "click a button below to choose a Stylometric test to run on this data:", font=FONT)
        self.label.grid(row = 1, column = 1)

        self.MendhallTest = Button(self, text = "Conduct Mendhall test:", font = FONT,  command = lambda : self.con.runMendenhall())
        self.MendhallTest.grid(row = 2, column = 1)


        self.sep = Label (self, text = "------------------------------------------------------------------", font = FONT)
        self.sep.grid(row = 3, column = 1)

        self.EnterAuthors = Label(self, text = "", font = FONT)
        self.EnterAuthors.grid(row = 6, column = 1)


                                                                                                                        # next up Kilgariff test, pretty straight forward, if the user did not enter disuputed as a author, then this section will not show up. Else if they did then they will get the following section built.

        self.notice = Label(self, text = "You do not have a 'Disputed' field! Cannot run a Kilgariff test!")
        self.notice.grid(row = 4, column = 1)

        self.kilgTest = Button(self, text = "Conduct Kilgariff test:", font = FONT, state=DISABLED, command = lambda : self.runTest(self.authorSelectedForKilg))
        self.kilgTest.grid(row=6, column = 2)

        self.lastRow = 7

        if(self.con.kilPossible()):
            self.kilgTest.grid_configure(row = 5, column = 3)

            self.notice.config(text = "")

            self.EnterAuthors.config(text = "how many authors do you want to compare in a kilgariff test? Check which ones:")

                                                                                                                        # this is a little check box area, the user checks which authors they want to have tested for the disputed files.
            allCurrentAuthors = self.con.returnAllAuthors()


            checkButtonDic = {}

            checkVariable = {}

            for x in  allCurrentAuthors:

                if(x != "Disputed"):
                    checkVariable[x] = IntVar()
                    checkButtonDic[x] = Checkbutton(self, text = str(x), variable = checkVariable[x]).grid(row = self.lastRow + 1, sticky = W)

                    self.lastRow += 1


            self.submit = Button(self,  text = "submit", command = lambda : self.selectedContent(checkVariable))        # submit once everything is checked.
            self.submit.grid(row = self.lastRow + 1, sticky = W)

            self.lastRow += 1


        self.sep2 = Label(self, text="------------------------------------------------------------------", font = FONT)
        self.sep2.grid(row = self.lastRow + 1, column = 1)

        self.lastRow += 1

        self.DeltaInst = Label(self, text = "Enter in the number of results that you would like to see for Word Frequency: *important, words will be removed if they are considerd a Stop word*", font= FONT)
        self.DeltaInst.grid(row = self.lastRow + 1, column = 1)

        self.ent = Entry(self)
        self.ent.grid(row = self.lastRow + 1, column = 2)

        self.lastRow += 1


        self.sub = Button(self, text = "Submit number", font = FONT, command = lambda : self.gainInfo())
        self.sub.grid(row = self.lastRow + 1, column = 1)
        self.lastRow += 1

        self.no = Label(self, text="", font=FONT)
        self.no.grid(row=self.lastRow + 1, column=2)
        self.lastRow += 1



    def closing(self):

        if (messagebox.askokcancel("Quit", "do you want to quit?")):
            self.root.destroy()
            #self.destroy()



    def gainInfo(self):



        if(len(self.ent.get()) == 0):

            self.no.config(text="please ensure a number within the entry!")

        else:

            x = int(self.ent.get())

            labelOfWord = {}

            counter = 0

            words = self.con.runDelta(x)

            perviousLR = self.lastRow

            while (counter < len(words)):



                if(counter < 25):

                    labelOfWord["word" + str(counter)] = Label(self, text = words[counter]).grid(row = self.lastRow + 1, column = 1)


                elif( counter < 50 and counter > 25 ):

                    if(counter == 26):
                        self.lastRow = perviousLR

                        labelOfWord["word" + str(counter)] = Label(self, text=words[counter]).grid(row=self.lastRow + 1, column=2)
                    else:

                        labelOfWord["word" + str(counter)] = Label(self, text=words[counter]).grid(row=self.lastRow + 1, column = 2)

                elif(counter < 75 and counter > 50):

                        if( counter == 51):
                            self.lastRow = perviousLR
                            labelOfWord["word" + str(counter)] = Label(self, text=words[counter]).grid(row=self.lastRow + 1, column=3)
                        else:
                            labelOfWord["word" + str(counter)] = Label(self, text=words[counter]).grid(row=self.lastRow + 1, column=3)

                elif counter < 100 and counter > 75 :

                    if (counter == 76):

                        self.lastRow = perviousLR

                        labelOfWord["word" + str(counter)] = Label(self, text=words[counter]).grid(row=self.lastRow + 1, column=4)

                    else:

                        labelOfWord["word" + str(counter)] = Label(self, text=words[counter]).grid(row=self.lastRow + 1, column=4)



                self.lastRow += 1
                counter += 1


    """
    selectedContent(checkVariable):
    
        param:
                checkVariable: this is a dictionary returned view, once the user clicks on one of the tick boxs above this dictionary containing the variables for that is stored here.
        
        this method counts through all the check box variables to see if it has been checked, if it has then we start the kilgariff test.
    """
    def selectedContent(self, checkVariable):

        self.authorSelectedForKilg.clear()



        for x in checkVariable.keys():

            num = checkVariable[x].get()

            if(num == 1):
                self.kilgTest.config(state=NORMAL)                                                                      # we can now conduct a test!
                self.authorSelectedForKilg.append(x)




    """
    RunText(author):
    
        param: author, a string of all the authors that were selected for testing.
        
        once the user has pressed Kilgariff test button above this method is called. Waits for the model to calculate the answers, return 
        it. It will be updated here and displayed on the view. 
        
    """
    def runTest(self, author):

        answers = self.con.runKilgariffTest(self.authorSelectedForKilg)
        self.answerL = Label(self, text = "Answers: ")
        self.answerL.grid( row = self.lastRow + 1, column = 1)
        ans = ""

        for keys, value in answers.items():

            ans += "Author: " + keys + " chisquare result is: " + str(value) + " "

            self.answerL.config(text = ans, font = FONT)



if __name__ == '__main__':

    root = tk.Tk()

    my_gui = startPage(root)


    root.mainloop()


