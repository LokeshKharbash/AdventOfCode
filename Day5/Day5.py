def readLineData(inputFile):
    with open("Day5/rulesinput.txt", 'r') as file1:
        rulesList = []
        for line in file1:
            rule = line.split("|")
            rule[0] = int(rule[0])
            rule[1] = int(rule[1])
            rulesList.append(rule)

    with open(inputFile, 'r') as file:
        inputStatement = ''
        arrays_list = []
        totalMiddleValue = 0
        inCorrectList = []

        for line in file:
            char_array = list(map(int, line.split(",")))
            i = 0
            ruleOutput = True
            while i < len(char_array) - 1:
                filtered_rules = list(filter(lambda a: a[0] == char_array[i] and a[1] == char_array[i+1], rulesList))
                if filtered_rules:
                    rule = filtered_rules[0]
                    if (rule[0] > rule[1] and char_array[i] > char_array[i+1]) or (rule[0] < rule[1] and char_array[i] < char_array[i+1]):
                        ruleOutput = True
                    else:
                        ruleOutput = False
                        break
                else:
                    ruleOutput = False
                    break
                i += 1
            if ruleOutput:
                # find middle integer of char_array
                middle = len(char_array) // 2
                if len(char_array) % 2 == 0:
                    middle_value = (char_array[middle - 1] + char_array[middle]) / 2
                else:
                    middle_value = char_array[middle]
                totalMiddleValue += middle_value
        print(totalMiddleValue)



readLineData("Day5/input.txt")