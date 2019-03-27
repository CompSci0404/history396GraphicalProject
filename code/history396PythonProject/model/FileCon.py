

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

    dataPath = ""

    def __init__(self, dataPath):
        self.dataPath = dataPath



    def buildText(self, allFiles, dataPath):

        textFileContent = []
        # for any kind of file per, author.
        # goal here is to add files into one large string, so I can compare them to other arthours.

        for file in os.listdir(dataPath):

            number = self.cutString(file)

            #if()

            #1 week extension. advance slide for power point transitions.

    def cutString(self, fileNameToCut):

        numberOfFile = int(re.search(r'\d+',fileNameToCut).group()) # library which makes string cutting very easy, just cut a number when it matches a deciminal.

        return numberOfFile

if __name__ == '__main__':
            test = FileCon("test")

            file = "federalist_1.txt"

            print(test.cutString(file))
