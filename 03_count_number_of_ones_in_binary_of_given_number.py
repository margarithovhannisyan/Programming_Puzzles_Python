'''
TASK - Count the number of ones in the binary representation of a given number
'''


def count_number_of_ones_in_binary_of_given_number(givenNumber):
    countOfOnes = 0
    if givenNumber == 0:
        return 0
    else:
        while givenNumber > 0:
            binaryNumber = givenNumber % 2
            givenNumber = givenNumber // 2
            if binaryNumber == 1:
                countOfOnes += 1
    return countOfOnes


# TEST
givenNumber = 79
result = count_number_of_ones_in_binary_of_given_number(givenNumber)
print("The count of ones in binary number of", givenNumber, "is", result)
