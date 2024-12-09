def readInputFile(inputFile):

    with open(inputFile, 'r') as file:
        list1 = []
        list2 = []
        for line in file:
            list1Item,list2Item = line.split("   ");
            list1.append(int(list1Item.strip()))
            list2.append(int(list2Item.strip())) 
        return list1, list2