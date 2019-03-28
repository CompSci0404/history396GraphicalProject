from model import authorConstruction
from model import FileCon


if __name__ == '__main__':


    test = FileCon("test")

    file = "federalist_0.txt"

    print(test.cutString(file))

    testDic = {"Madison": [10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
               "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                            25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                            61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                            78, 79, 80, 81, 82, 83, 84, 85],
               "Jay": [2 ,3 ,4 ,5], }

    tester = authorConstruction.authorConstruction(testDic)


    author_PaperContent = {}
    dataDir = "C:/Schoolprojects/history papers/history396project/history396GraphicalProject/Data/data"

    for author, fileNum in tester.papersByAuthor.items():

        author_PaperContent[author] = test.buildText(fileNum, dataDir )


    print("HELLO?" ,author_PaperContent)
