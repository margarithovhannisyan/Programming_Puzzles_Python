'''
TASK - Get binary number of given integer
'''


def get_binary_number_of_integer(givenNumber):
    countOnes = 0
    if givenNumber == 0:
        return 0
    else:
        while givenNumber > 0:
            binaryNumber = givenNumber % 2
            givenNumber = givenNumber // 2
            if binaryNumber == 1:
                countOnes += 1
    return countOnes


# TEST
givenNumber = 42
result = get_binary_number_of_integer(givenNumber)
print("The count of ones in binary number of", givenNumber, "is", result)
