def readLineData(inputFile):

    with open(inputFile, 'r') as file:
        inputStatement=''
        arrays_list = []
        for line in file:
            char_array = list(line.strip())
            arrays_list.append(char_array)
        
        # getXmaSWordCount(arrays_list)
        getMasinShapeOfX(arrays_list)

def getXmaSWordCount(arrays_list):
    count = 0
    rows = len(arrays_list)
    cols = len(arrays_list[0]) if rows > 0 else 0
    currentRow = -1

    # Horizontal check
    for array in arrays_list:
        currentRow += 1
        i = 0
        while i < len(array):
            if array[i] == 'X':
                if i + 1 < len(array) and array[i + 1] == 'M':
                    if i + 2 < len(array) and array[i + 2] == 'A':
                        if i + 3 < len(array) and array[i + 3] == 'S':
                            count += 1
                if (i > 3):
                    if array[i] == 'X':
                        if array[i - 1] == 'M':
                            if array[i - 2] == 'A':
                                if array[i - 3] == 'S':
                                    count += 1
            #Vertical Down check
                if currentRow + 3 < rows:
                   if arrays_list[currentRow + 1][i] == 'M':
                      if arrays_list[currentRow + 2][i] == 'A':
                         if arrays_list[currentRow + 3][i] == 'S':
                            count += 1
                    # check diagonaly down forward
                   if i < cols - 3:
                        if arrays_list[currentRow + 1][i + 1] == 'M':
                            if arrays_list[currentRow + 2][i + 2] == 'A':
                                if arrays_list[currentRow + 3][i + 3] == 'S':
                                    count += 1
                    # check diagonaly backwords
                   if i > 3:
                        print("current row down diagonal backwards: " ,int(currentRow))
                        print(i)
                        if arrays_list[currentRow + 1][i - 1] == 'M':
                            if arrays_list[currentRow + 2][i - 2] == 'A':
                                if arrays_list[currentRow + 3][i - 3] == 'S':
                                    count += 1
            #Vertical Up check
                if currentRow - 2 > 0:
                     print("current row upwards : " ,int(currentRow))
                     print(i)
                     if arrays_list[currentRow - 1][i] == 'M':
                         if arrays_list[currentRow - 2][i] == 'A':
                             if arrays_list[currentRow - 3][i] == 'S':
                                count += 1
                    # check diagonaly up
                     if i < cols - 3:
                            if arrays_list[currentRow - 1][i + 1] == 'M':
                                if arrays_list[currentRow - 2][i + 2] == 'A':
                                    if arrays_list[currentRow - 3][i + 3] == 'S':
                                        count += 1
                     if i > 3:
                        if arrays_list[currentRow - 1][i - 1] == 'M':
                            if arrays_list[currentRow - 2][i - 2] == 'A':
                                if arrays_list[currentRow - 3][i - 3] == 'S':
                                    count += 1
            i += 1
 
    print(count)

def getMasinShapeOfX(arrays_list):
    count = 0
    rows = len(arrays_list)
    cols = len(arrays_list[0]) if rows > 0 else 0
    currentRow = -1

    # Horizontal check
    for array in arrays_list:
        currentRow += 1
        i = 0
        while i < len(array) - 2:
            if ((array[i] == 'M' and array[i+2] == 'S') or (array[i] == 'S' and array[i+2] == 'M')) :
            #Vertical Down check
                if currentRow + 3 < rows:
                    # check diagonaly down forward
                   if i < cols - 2:
                        if arrays_list[currentRow + 1][i + 1] == 'A':
                            if (array[i] == 'M' and array[i+2] == 'S'): 
                                if arrays_list[currentRow + 2][i + 2] == 'S' and arrays_list[currentRow + 2][i] == 'M':
                                    count += 1
                            else:
                                if arrays_list[currentRow + 2][i + 2] == 'M' and arrays_list[currentRow + 2][i] == 'S':
                                    count += 1
                if currentRow - 1 > 0:
                    # check diagonaly up
                     if i < cols - 3:
                        if arrays_list[currentRow - 1][i + 1] == 'A':
                            if (array[i] == 'M' and array[i+2] == 'S'):
                                if arrays_list[currentRow - 2][i + 2] == 'S' and arrays_list[currentRow - 2][i] == 'M':
                                    count += 1
                            else:
                                if arrays_list[currentRow - 2][i + 2] == 'M' and arrays_list[currentRow - 2][i] == 'S':
                                    count += 1
            #Vertical Up check
            i += 1
 
    print(count)

readLineData("Day4/input.txt")