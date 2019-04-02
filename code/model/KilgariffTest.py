

import nltk
from model import FileCon
class KilgariffTest:

    def __init__(self):
        pass


    def buildToken(self, dataBase):


        databaseToken = {}

        for keys,value in dataBase.items():

            tokens = nltk.word_tokenize(dataBase[keys])
            databaseToken[keys] = ([token for token in tokens if any(c.isalpha() for c in token)] )

            print(keys)

        return databaseToken


    """
    runKilgariffText(database, authors)
    
        Paramter: 
                    database: the data in which we are running the kilgarif test on. 
                    authors: the authors we want to compare to the disputed papers. 
                    
                     
        builds tokens so NLTK can run a kilgariff chi square test on the data base. The important factor with this test is we need a Disputed
        field in order to run it. In other words we need data in which we do not know who authored it. This tests checks to see which author could have
        possibly written the text. 
    
    """
    def runKilgariffTest(self,database, authors):


            database_Token = self.buildToken(database)  # build tokens before using


            for author in authors:

                database_Token[author] = ([token.lower() for token in database_Token[author]])
                database_Token["Disputed"] = ([token.lower() for token in database_Token["Disputed"]])

            # find the CHI square:
            for author in authors:

                joint_corpus = (database_Token[author] + database_Token["Disputed"])    # combine the papers from the disputed dictionary, and author.

                joint_freq_dist = nltk.FreqDist(joint_corpus)                           # grabe the frequent distrubtion.

                most_common = list(joint_freq_dist.most_common(500))

                author_share = (len(database_Token[author])/ len(joint_corpus))


                chisquared = 0
                for word, joint_count in most_common:                                   # calculations for ChiSquare, basically we will calculate to see which words are similar between both Disputed and non disputed.

                    author_count = database_Token[author].count(word)
                    disputed_count = database_Token["Disputed"].count(word)


                    expected_author_count = joint_count * author_share
                    expected_disputed_count = joint_count * (1 - author_share)

                    chisquared += ((author_count - expected_author_count) *
                                   (author_count - expected_author_count) /
                                   expected_author_count)

                    chisquared += ((disputed_count - expected_disputed_count) *
                                   (disputed_count - expected_disputed_count)
                                   / expected_disputed_count)


                print("The Chi-squared statistic for candidate", author, "is", chisquared)








if __name__ == '__main__':

    test = KilgariffTest()

    authors = ("Jay", "Madison")

    testDic = {"Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
               "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                            61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                            78, 79, 80, 81, 82, 83, 84, 85],
               "Jay": [2, 3, 4, 5],

               "Shared": [18, 19, 20],

               "Disputed": [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63],
               "testCase": [64]}

    testFile = FileCon.FileCon()

    dataPath = "C:/Schoolprojects/history papers/history396project/history396GraphicalProject/Data/data"

    testFile.buildData(testDic, dataPath)

    test.runKilgariffTest(testFile.dataBase, authors)

