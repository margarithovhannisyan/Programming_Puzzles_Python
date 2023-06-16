'''
TASK - Calculate the sum of all the multiples of 3 or 5 below a given number
DESCRIPTION - Given an integer number, output the sum of all the multiples of 3 and 5 below that number.
If a number is a multiple of both, 3 and 5, it should appear in the sum only once. '''


def calculate_sum_of_multiples(givenNumber):
    result = 0
    for currentNumber in range(givenNumber):
        if currentNumber % 3 == 0 or currentNumber % 5 == 0:
            result += currentNumber
    return result


# TEST
givenNumber = 100
result = calculate_sum_of_multiples(givenNumber)
print("The sum of all multiples of 3 or 5 below", givenNumber, "is:", result)
