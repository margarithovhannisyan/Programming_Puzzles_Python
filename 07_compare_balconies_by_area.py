'''
You are trying to determine which of two apartments has a larger balcony.
Both balconies are rectangles, and you have the length and width, but you need the area.

Task
Evaluate the area of two different balconies and determine which one is bigger.

Input Format
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.
'''

def calculate_balcony_area(length, width):
    return length * width


def compare_balconies_by_area(balcony1_length, balcony1_width, balcony2_length, balcony2_width):
    balcony1_area = calculate_balcony_area(balcony1_length, balcony1_width)
    balcony2_area = calculate_balcony_area(balcony2_length, balcony2_width)
    if balcony1_area > balcony2_area:
        return "Balcony 1 is larger."
    elif balcony2_area > balcony1_area:
        return "Balcony 2 is larger."
    else:
        return "Both balconies have the same area."


# TEST
balcony1_length = 5
balcony1_width = 5
balcony2_length = 1
balcony2_width = 5

result = compare_balconies_by_area(balcony1_length, balcony1_width, balcony2_length, balcony2_width)
print(result)
