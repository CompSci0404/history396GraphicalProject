
from model import authorConstruction


class controller:

    authorData = None

    def __init__(self):
        pass


    def authorBuild(self, authorAndFileNum):

        self.authorData = authorConstruction.authorConstruction(authorAndFileNum)

        print("made it in here! this is the data:", self.authorData.returnCopy())