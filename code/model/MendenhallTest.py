# this is first test that can be ran on the system, Mendenhalls curves test.

import nltk
nltk.download('punkt')

import matplotlib.pyplot as plt

from model import FileCon
from model import authorConstruction





class MendenhallTest:



    def __init__(self):
        pass



    def runMendenhalTest(self, dataBase):

        fed_By_Token =  {}

        fed_len_dis = {}



        for author, value in dataBase.items():

            tokens = nltk.word_tokenize(dataBase[author])

            fed_By_Token[author]= ([token for token in tokens
                                if any(c.isalpha() for c in token)])

            token_len = [len(token) for token in fed_By_Token[author]]



            fed_len_dis[author] = nltk.FreqDist(token_len)
            fed_len_dis[author].plot(15, title=author)



    # going to need to use plt to run this stuff!







if __name__ == '__main__':

    menTest = MendenhallTest()

    testDic = {"Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
               "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                            61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                            78, 79, 80, 81, 82, 83, 84, 85],
               "Jay": [2, 3, 4, 5], }

    authorCon = authorConstruction.authorConstruction(testDic)
    fileConstruction = FileCon.FileCon()



    author_PaperContent = {}
    dataPath = "C:/Schoolprojects/history papers/history396project/history396GraphicalProject/Data/data"



    author_PaperContent = fileConstruction.buildData(author_PaperContent, authorCon.returnCopy(), dataPath)


    print("running mendenhalTest!:")
    menTest.runMendenhalTest(author_PaperContent)






