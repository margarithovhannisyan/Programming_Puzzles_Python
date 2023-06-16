'''
TASK - Get binary number of given integer
'''


def get_binary_number_of_integer(givenNumber):
    binaryList = []
    if givenNumber == 0:
        return 0
    else:
        while givenNumber > 0:
            binaryNumber = givenNumber % 2
            binaryList.insert(0, binaryNumber)
            givenNumber = givenNumber // 2
    return binaryList


# TEST
givenNumber = 42
result = get_binary_number_of_integer(givenNumber)
print("The binary number of", givenNumber, "is:", result)
