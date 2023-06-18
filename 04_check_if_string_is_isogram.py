'''
TASK - Check if given String is an isogram or not. If it is, output True, or False, if it is not
DESCRIPTION - An isogram is a word that has no repeating letters
'''


def is_isogram(givenString):
    givenString = str(givenString).lower()
    for i in range(len(givenString)):
        letter = givenString[i]
        if letter in givenString[i + 1:]:
            return False
    else:
        return True


# TEST
print(is_isogram("HeLlo"))
print(is_isogram(22))
