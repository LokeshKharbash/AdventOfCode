inputFile = "Day2/input.txt"

def readLineData(inputFile):

    with open(inputFile, 'r') as file:
        safeCount=0
        for line in file:
            line = line.strip()
            list2 = line.split(" ");
            # print(list2)
            safe = getSafeFlag(list2)
            if safe:
                print("Safe")
                safeCount+=1
            else:
                print(list2)
        print(safeCount)

def getSafeFlag(list):
    listAscending = False
    if int(list[0]) < int(list[1]):
        listAscending = True
    
    for i in range(len(list) - 1):
        if listAscending:
            if int(list[i]) > int(list[i+1]):
                print("List is not in ascending order")
                return False
        else:
            if int(list[i]) < int(list[i+1]):
                print(list[i] + " " + list[i+1])
                print("List is not in descending order")
                return False
        
        if abs(int(list[i]) - int(list[i+1])) > 3:
            print("Difference is greater than 3")
            return False
        if abs(int(list[i]) - int(list[i+1])) < 1:
            print("Difference is less than 1")
            return False
    return True


readLineData(inputFile)
