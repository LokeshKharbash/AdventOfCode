def readLineData(inputFile):

    with open(inputFile, 'r') as file:
        inputStatement=''
        arrays_list = []
        for line in file:
            char_array = list(line.strip())
            arrays_list.append(char_array)
        
        convertedIDBlocks = convertIdBlocks(char_array)
        print(convertedIDBlocks)
        moveddotToend = replacedotwithFirstID(convertedIDBlocks)
        print(moveddotToend)
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

def replacedotwithFirstID(char_array):
    readChar = len(char_array) - 1
    for i in range(len(char_array)):
        if char_array[i] == '.':
            runLoop = True
            while readChar > i and runLoop:
                runLoop = True
                if char_array[readChar] == '.':
                   readChar -= 1
                else:
                    char_array[i] = char_array[readChar]
                    char_array[readChar] = '.'
                    runLoop = False
                print("readChar: ",readChar," i: ",i)
        
    return char_array    

readLineData("Day9/input.txt")