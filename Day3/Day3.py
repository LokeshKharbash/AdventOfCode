import re

def readLineData(inputFile):

    with open(inputFile, 'r') as file:
        inputStatement=''
        for line in file:
            inputStatement+=line
        pattern = r"don't\(\).*?do\(\)"

        # Replace all matched text with an empty string
        cleaned_statement = re.sub(pattern, '', inputStatement)
        don't = cleaned_statement.find("don't","")
        print(cleaned_statement)
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, cleaned_statement)
        getSumOfMultiplication(matches)

def getSumOfMultiplication(matches):
    sum=0
    for match in matches:
        match = match.replace("mul(","")
        match = match.replace(")","")
        match = match.split(",")
        sum+=int(match[0])*int(match[1])
    print(sum)
readLineData("Day3/input.txt")
