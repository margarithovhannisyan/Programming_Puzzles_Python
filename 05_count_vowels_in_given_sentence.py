'''
TASK - Check how many vowels are there in given sentence
DESCRIPTION - Vowels are the glue that hold words and sentences together
'''

vowels = "aeiou"


def count_vowels(sentence):
    countVowels = 0
    for i in sentence:
        if i.lower() in vowels:
            countVowels += 1
    return countVowels


givenSentence = count_vowels("This is A Sentence")
print(f"There are {givenSentence} vowels in given sentence")
