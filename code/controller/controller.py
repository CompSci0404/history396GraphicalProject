
from model import authorConstruction
from model import FileCon
from model import MendenhallTest
from model import KilgariffTest
from model import DeltaTest

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



    def runKilgariffTest(self, authors):

        runKil = KilgariffTest.KilgariffTest()

        answer = runKil.runKilgariffTest(self.fileConRef.dataBase, authors)

        print(answer)


        return answer


    def kilPossible(self):

        keyExist = False

        if "Disputed" in self.fileConRef.dataBase:

            keyExist = True


        return keyExist


    def returnAllAuthors(self):

        return self.authorDataRef.returnAuthors()



    def runDelta(self, num):

        delt = DeltaTest.DeltaTest()

        self.returnAllAuthors()

        list = delt.runDeltaTest(self.fileConRef.dataBase, self.returnAllAuthors(), num)

        return list
