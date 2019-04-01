
from model import authorConstruction
from model import FileCon
from model import MendenhallTest

class controller:

    authorDataRef = None
    fileConRef = None


    def __init__(self):
        pass


    def authorBuild(self, authorAndFileNum, dataPath):

        self.authorDataRef = authorConstruction.authorConstruction(authorAndFileNum)
        self.fileConRef = FileCon.FileCon()

        self.fileConRef.buildData(self.authorDataRef.returnCopy(), dataPath)


       # print("made it in here! this is the data:", self.authorDataRef.returnCopy())

        #print("Here is the finished Data base:", self.fileConRef.dataBase) # data base built!


    def runMendenhall(self):

        runMen = MendenhallTest.MendenhallTest()

        runMen.runMendenhalTest(self.fileConRef.dataBase)

