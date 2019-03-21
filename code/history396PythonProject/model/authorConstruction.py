
import copy



"""

python class, which contains a data structure called a dictionary of Lists, its job is to store all the
text files that the user selected into the correct author that the user gave us in the VIEW.

"""

class authorConstruction:

    papersByAuthor = {}




    def __init__(self, papersByAuthor):

        self.papersByAuthor = papersByAuthor


    """
    toString():
        Prints out all the data that is held by the papers by authors, a way to visualize 
        all the content on the console. It transforms data into a string, so I can print out data.
        
        returns: Returns a string containing all data found within the dictionary.
    """

    def toString(self):

        #I will propbably just use a string, for this project, however for larger amounts of a data a list is probably better.

        contentsOfDic = ""  #string containing all content found within the dictionary.
        listOfItems = []    # list of all the content found in dictionarys values.

        for author in self.papersByAuthor:  # count through all content, and add to string to print out.
            counter = 0

            contentsOfDic += "\n" + str(author) +":"+ "\n"
            listOfItems = self.papersByAuthor[author]

            while(counter < len(listOfItems)):

                contentsOfDic += str(listOfItems[counter]) + " "

                counter +=1


        return contentsOfDic


    """
    :returnDictionaryLenght(): 
    
        returns the current length of this dictionary. 
        
        return: a integer number that is the length of the dictionary.
    """
    def returnDictionaryLength(self):

        return len(self.papersByAuthor)



    """
    returnDictionary(): 
    
        returns the dictionary, if I ever need to use a copy or clone of the data this method would be called.
        the point is so that nothing is referenced when mainpulating data, I am not using the models main data. This
        could lead to the original being touched.
        
        return: a cloned dictionary.
    """
    def returnCopy(self):

        deepCopy = copy.deepcopy(self.papersByAuthor)

        return deepCopy





if __name__ == '__main__':
    # for testing of this class!

    testDic = { "marcfallen":[10, 20, 15, 25, 40],
                "howard":[25, 35, 1],
                "Shared": [12], }


    buildAuthor = authorConstruction(testDic)   # build auhtor construction.

    if(buildAuthor != None):


        print("successfully built author class")
    else:

        print("failed to build author test failed!")


    if(buildAuthor.returnDictionaryLength() == 3):

        print("lenght is returning correct variable content.")
    else:

        print("len is wrong not returning correct value!")

    newDic = buildAuthor.returnCopy()

    if(newDic != None):

        print("built a new dictionary no propblem!")

    else:
        print("did not build a new dictionary!")

    print("all content inside copied dictionary:\n",newDic)

# read data for tostring, should print out all content.
    print(buildAuthor.toString())
