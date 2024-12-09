def readLineData(inputFile):

    with open(inputFile, 'r') as file:
        inputStatement=''
        arrays_list = []
        for line in file:
            char_array = list(line.strip())
            arrays_list.append(char_array)
        
        convertedIDBlocks = convertIdBlocks(char_array)
        # print(convertedIDBlocks)
        moveddotToend = replacedotwithFirstID(convertedIDBlocks)
        # print(moveddotToend)
        checksum = 0
        for i in range(len(moveddotToend) - 1):
            if moveddotToend[i] != '.':
                checksum += int(moveddotToend[i]) * i
                
        print(checksum)

def convertIdBlocks(char_array):
    id = 0
    convertIdBlocks = []

    for i in range(len(char_array)):
        print("id:",id," character: ",char_array[i]," iteration: ",i)
        if i%2 == 0:
            for j in range(int(char_array[i]) ):
                convertIdBlocks.append(str(id))
            id += 1
        else:
            for j in range(int(char_array[i]) ):
                convertIdBlocks.append('.')
        

    return convertIdBlocks
def getContinousDotCharsFromStart(char_array,dotCount,endposition):
    print("dotCount: ",dotCount)
    positionFound = False
    continousCount = 0
    startPosition = 0
    i = 0
    while i < len(char_array) and i < endposition:
        if char_array[i] == '.':
            j = i
            while j < len(char_array) and char_array[j] == '.':
                continousCount += 1
                j += 1
            
            if continousCount >= dotCount:
                positionFound = True
                print("i: ",i," dotCount: ",continousCount)
                startPosition = i  
                break
            else:
                continousCount = 0
                i = j
        continousCount = 0
        i += 1

    return positionFound,startPosition

def replacedotwithFirstID(char_array):
    startPosition = 0
    replaceArray = []
    continousCount = 1
    readChar = len(char_array) - 1
    i = len(char_array) - 1
    while 0 < i <= readChar:
        if char_array[i] != '.':
            startLetter = char_array[i]
            j = i
            while j > 0 and char_array[j] == startLetter:
                continousCount += 1
                replaceArray.append(char_array[i])
                j -= 1
            
            positionFound,startPosition = getContinousDotCharsFromStart(char_array,continousCount,i)
            if positionFound:
                    for k in range(len(replaceArray)):
                        char_array[startPosition + k] = replaceArray[k]
                        
                        char_array[i - k] = '.'
            i = j
            print("i:",i) 
            continousCount = 0
            replaceArray = []
        else:
            i -= 1
    print("startPosition: ",startPosition)
    return char_array
    return 

readLineData("Day9/input.txt")