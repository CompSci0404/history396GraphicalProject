
# Matt Radke
# mmr174

import os
import re


"""
the point of this class, is to build all the text for each piece of writing.
we need to find gain the correct file and add it to a list which we can store with
the correct author. This will allow us to compare texts between two or more authors.
"""


class FileCon:


    """
    init method, constructor for this class.
    """
    def __init__(self):
        pass        # pass, there is not instance variables that need to be defined.





    """
    buildText(filesBelongToAuthor, dataPath):
        filesBelongToAuthor: a list of integers, repersenting file numbers that belong to a certian author.
        dataPath: a string, that contains the pathway to the data we are searching for.
        
        finds a file that belongs to a certain author appends text file to a string then returns that entire lists that repsents all the text files together.
    """

    def buildText(self, filesBelongToAuthor, dataPath):
        text = []                   # the text that needs to be returned.
        savedPath = dataPath        # saves the data

        for files in os.listdir(dataPath):  #  counting through files within a directory.


            if(files.endswith(".txt")):

                fileNum = self.cutString(files)     # grab the number of a certian file.

                for numb in filesBelongToAuthor:

                    dataPath = savedPath

                    if(fileNum == numb ):           # if file number is equal to the number for a certian author, found our match.

                        #print("MATCH FOUND!")

                        dataPath += "/" + files     # aquire the file in the data path.

                        with open(dataPath) as f:   # open up the file and add it to the list.
                            text.append(f.read())

        return '\n'.join(text)

    """
    cutString(fileNameToCut):
    
        fileNameToCut: the file in which we want to aquire the number from, in file.
        
        cuts a string and returns a number.
        
        returns: A number, that represent which file it is.
    """

    def cutString(self, fileNameToCut):

        numberOfFile = int(re.search(r'\d+'
                                     ,fileNameToCut).group()) # library which makes string cutting very easy, just cut a number when it matches a deciminal.

        return numberOfFile


    """
    buildData(dictionary, DictionaryValues, dataPath):
        dictionary: text documents that are appended to a certian author.
        DictionaryValues: The list of numbers which states what text belongs to a certian author.
        dataPath: the file directory which contains all the text files in a certain directory. 
        
        build a dictionary, which contains a 'data base', which contains all data that will need to be used to run
        stylometeric tests. 
    """
    def buildData (self, dataBase, DictionaryValues, dataPath):

        for author, values in DictionaryValues.items():
            dataBase[author] = self.buildText(values, dataPath)


        return dataBase

if __name__ == '__main__':

    test = FileCon()

    testDic = {"Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
               "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                            61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                            78, 79, 80, 81, 82, 83, 84, 85],
               "Jay": [2 ,3 ,4 ,5], }

    author_PaperContent = {}

    dataPath = "C:/Schoolprojects/history papers/history396project/history396GraphicalProject/Data/data"

    author_PaperContent= test.buildData(author_PaperContent, testDic, dataPath)

    # test to see if we are getting correct file output.
    for author in testDic:

        print(author_PaperContent[author][:200])



