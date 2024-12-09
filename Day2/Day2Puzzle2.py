inputFile = "Day2/input.txt"

def readLineData(inputFile):

    with open(inputFile, 'r') as file:
        safeCount=0
        for line in file:
            line = line.strip()
            list2 = line.split(" ");
            # print(list2)
            safe,errorItemPosition,errorItemPosition2main = getSafeFlag(list2)
            if safe:
                print("Safe")
                safeCount+=1
            else:
                list2.remove(str(errorItemPosition))
                safe,errorItemPosition,errorItemPosition2 = getSafeFlag(list2)
                if safe:
                    print("Safe")
                    safeCount+=1
                else:
                    list2 = line.split(" ");
                    list2.remove(str(errorItemPosition2main))
                    safe,errorItemPosition,errorItemPosition2main = getSafeFlag(list2)
                    if safe:
                        print("Safe")
                        safeCount+=1
                    else:
                        print(list2)
        print(safeCount)

def getSafeFlag(list):
    listAscending = is_generally_ascending_or_descending(list)

    
    for i in range(len(list) - 1):
        if listAscending:
            if int(list[i]) > int(list[i+1]):
                print("List is not in ascending order" )
                return False,list[i], list[i+1]
        else:
            if int(list[i]) < int(list[i+1]):
                print(list[i] + " " + list[i+1])
                print("List is not in descending order")
                return False,list[i], list[i+1]
        
        if abs(int(list[i]) - int(list[i+1])) > 3:
            print("Difference is greater than 3")
            return False,list[i], list[i+1]
        if abs(int(list[i]) - int(list[i+1])) < 1:
            print("Difference is less than 1")
            return False,list[i],list[i+1]
    return True, 0,0

def is_generally_ascending_or_descending(lst):
    lst = [int(x) for x in lst]
    ascending_errors = 0
    descending_errors = 0

    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            descending_errors += 1
        elif lst[i] > lst[i + 1]:
            ascending_errors += 1

    # Allow one error in the list
    if ascending_errors <= 1:  
        return True
    return False

readLineData(inputFile)

