
import nltk
from model import FileCon
import re
nltk.download('stopwords')


class DeltaTest:

    def __init__(self):
        pass


    def buildToken(self, dataBase):
        databaseToken = {}

        for keys, value in dataBase.items():

            tokens = nltk.word_tokenize(dataBase[keys])
            databaseToken[keys] = ([token for token in tokens if any(c.isalpha() for c in token)])

        return databaseToken


    """
    
    runDeltaTest(database, authors, numberOfWordShown):
    
        database: the pieces of text that we are working with.
        authors: the authors that are included within this test of counting all words in the corpus. I think by default it is all authors.
        For now though, I will keep like this incase I ever want to keep working on this project.
        numberOfWordShown: the number big words we want to display.
        
        This method will calculate all the words and the numbers of times it appears within the all the texts combined. After aquiring the words, they will be put through a filter to remove
        all the stopwords, within it. These would be considered as The, as, to,etc. types of words.
    
    """
    def runDeltaTest(self, dataBase, authors , numberOfWordShown):

        dataBase_Token = self.buildToken(dataBase)

        # Combine every paper except our test case into a single corpus
        whole_corpus = []
        whole_corpus_freq_dist = []

        stopwords = nltk.corpus.stopwords.words('english')

        """
        Stop words, this libary above gives me a list of words which are common, however there is still some verisions of words that are not caught.
        Any capitals verisons of the majority of Stop words are not caught in the list. I added onto the Stop words list in attempt to increase percision.
    
        """

        stopwords.append("The")
        stopwords.append("It")
        stopwords.append("I")
        stopwords.append("In")
        stopwords.append("This")
        stopwords.append("And")
        stopwords.append("THE")
        stopwords.append("They")
        stopwords.append("These")
        stopwords.append("There")
        stopwords.append("If")
        stopwords.append("To")
        stopwords.append("Has")
        stopwords.append("As")
        stopwords.append("But")

        for author in authors:
            whole_corpus += dataBase_Token[author]

            # I tried a few ways to remove Stop words, a very bad idea is to attempt to remove them from the corpus. Two reasons, First we are manipulating the Raw data.
            #Second, it litterally takes O(N) time to count through every word in a text file. Then put that O(N) to the power of re counting throw it to find a stop word each time.
            # So roughly I think it is around O(N)^N

            # Get a frequency distribution
            whole_corpus_freq_dist = list(nltk.FreqDist(whole_corpus).most_common(numberOfWordShown))


        return self.cleanData(whole_corpus_freq_dist, stopwords)

    """
    cleansData(corpus, stopwords):
    
        corpus: The list of tuples, containg the most used words within a piece of literature. 
        stopwords: the words we sadly do not care about, IE the. 
        
        returns: A cleaned verision of the corpus.
    """
    def cleanData(self, whole_corpus_freq_dist, stopwords):

        # count through each stop word, as we count through the word, we will check the entire corpus, if we find a match remove it from the corpus. Time complexity is WAY quicker.
        for stp in stopwords:
            for i in whole_corpus_freq_dist:
                if (i[0] == stp):
                    whole_corpus_freq_dist.remove(i)


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

    print(test.runDeltaTest(testFile.dataBase, authors, 300))
