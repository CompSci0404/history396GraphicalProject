
import nltk
import math
from model import FileCon

class DeltaTest:

    def __init__(self):
        pass


    def buildToken(self, dataBase):
        databaseToken = {}

        for keys, value in dataBase.items():
            tokens = nltk.word_tokenize(dataBase[keys])
            databaseToken[keys] = ([token for token in tokens if any(c.isalpha() for c in token)])

            print(keys)

        return databaseToken


    def runDeltaTest(self, dataBase, authors, numberOfWordShown):


        dataBase_Token = self.buildToken(dataBase)

        # Combine every paper except our test case into a single corpus
        whole_corpus = []

        for author in authors:

            whole_corpus += dataBase_Token[author]

        # Get a frequency distribution
        whole_corpus_freq_dist = list(nltk.FreqDist(whole_corpus).most_common(numberOfWordShown))

        return whole_corpus_freq_dist






if __name__ == '__main__':

    test = DeltaTest()

    authors = ("Jay", "Madison", "Hamilton", "Shared", "Disputed", "TestCase")

    testDic = {"Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
               "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                            61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                            78, 79, 80, 81, 82, 83, 84, 85],
               "Jay": [2, 3, 4, 5],

               "Shared": [18, 19, 20],

               "Disputed": [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
               "TestCase": [64]}

    testFile = FileCon.FileCon()

    dataPath = "C:/Schoolprojects/history papers/history396project/history396GraphicalProject/Data/data"

    testFile.buildData(testDic, dataPath)

    test.runDeltaTest(testFile.dataBase, authors)
