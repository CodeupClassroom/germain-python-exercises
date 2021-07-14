def get_letter_grade(number):
    if number <= 69:
        grade = "F"
    elif number <= 79:
        grade = "C"
    elif number <= 89:
        grade = "B"
    else:
        grade = "A"
    return grade


def calculate_tip(bill, tip_percent):    
    return bill * tip_percent


def is_vowel(x):
    # Anything not a string is definitely not a vowel
    if type(x) != str:
        return False

    x = x.lower() # lowercase the input
    
    return x in ["a", "e", "i", "o", "u"] # return a boolean


def is_consonant(x):
    if type(x) != str:
        return False

    result = not is_vowel(x) and x.isalpha()
    return result


# Procedural code indented here will only run if we explicitly run this file from the command line
if __name__ == '__main__':
    letter = "A"
    print(f"Is the letter {letter} a vowel? {is_vowel(letter)}")
    print(f"Is the letter {letter} a consonant? {is_consonant(letter)}")

    # print() prints an empty new line
    print() 

    letter = "B"
    print(f"Is the letter {letter} a vowel? {is_vowel(letter)}")
    print(f"Is the letter {letter} a consonant? {is_consonant(letter)}")

    print() 

    letter = "X"
    print(f"Is the letter {letter} a vowel? {is_vowel(letter)}")
    print(f"Is the letter {letter} a consonant? {is_consonant(letter)}")

    print()

    letter = "E"
    print(f"Is the letter {letter} a vowel? {is_vowel(letter)}")
    print(f"Is the letter {letter} a consonant? {is_consonant(letter)}")

    print()
    letter = "$"
    print(f"Is the letter {letter} a vowel? {is_vowel(letter)}")
    print(f"Is the letter {letter} a consonant? {is_consonant(letter)}")
