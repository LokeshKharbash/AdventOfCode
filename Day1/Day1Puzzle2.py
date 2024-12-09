
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Helper.ReadData.ReadInputData import readInputFile
list1,list2 = readInputFile("Day1/input.txt")

def getSimilarityScore(list1, list2):
    list1.sort()
    list2.sort()
    similarityscore = 0
    biggerList = list1 if len(list1) >= len(list2) else list2
    smallerList = list2 if len(list1) >= len(list2) else list1
    for i in range(len(biggerList)):
         similarityscore += biggerList[i] * smallerList.count(biggerList[i])
    
    return similarityscore

distance = getSimilarityScore(list1, list2)
print(distance)

