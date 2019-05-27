"""
Name:Elijah Espiritu
ID: 018679581
Instructor: Neal Terrell
Date: 3/19/19
Purpose: A Man A Plan, A Canal: Panama
"""
import EnglishDictionary


def print_menu():
    print("1. Check a phrase to see if it's a palindrome \n"
          "2. Check N many words to see if it/they form a crossword square \n"
          "3. Quit")


def get_menu_choice():
    user_choice = int(input("Choose a function: "))
    # Validation
    while user_choice < 1 or user_choice > 3:
        user_choice = int(input("Invalid Input, Choose a function: "))
    return user_choice


def get_phrase():
    user_phrase = input("Enter a phrase: ")
    # Validation
    while len(user_phrase) < 1:
        user_phrase = input("Invalid, length must be > 0. Enter a phrase: ")
    return user_phrase


def is_palindrome(phrase):
    # Make the phrase all lowercase then evaluate the string, skipping over non-letters
    phrase = phrase.lower()
    i = 0
    j = len(phrase) - 1
    letter = 0
    # Since a string containing no letters is a palindrome, find out if phrase has at least one letter. If a letter is
    # found, the phrase needs to be evaluated
    for ch in phrase:
        if ch.isalpha() and letter == 0:
            letter += 1
    if letter == 1:
        while i < j:
            # If i is not is not a letter, loop until the index is on a letter. Repeat for j
            while not phrase[i].isalpha():
                i += 1
            while not phrase[j].isalpha():
                j -= 1
            else:
                # Indicates the phrase is not a palindrome
                if phrase[i] != phrase[j]:
                    return False
            i += 1
            j -= 1
        # Indicates i and j were the same until i = j, meaning the phrase is a palindrome
        return True
    # The phrase consists only of non-letters, making it a palindrome
    return True


def menu_check_palindrome():
    user_phrase = get_phrase()
    palindrome = is_palindrome(user_phrase)
    if palindrome:
        print("{0} is a palindrome!".format(user_phrase))
    else:
        print("{0} is not a palindrome.".format(user_phrase))


def get_crossword_square():
    # First line establishes the order N of the square depending on its length
    crossword_square = input("Enter the first word of the square: ")
    # The next words should be inputted N - 1 more times and should be the same length as N
    for i in range(len(crossword_square) - 1):
        crossword_square += input("Enter the next word of the square: ")
    return crossword_square


def check_crossword_square(square):
    # Make the square all lowercase so it can be read in words_alpha.txt
    square = square.lower()
    # Calculate order by square rooting len of square
    square_root = 1 / 2
    order = int(len(square) ** square_root)
    horiz_word = True
    verti_word = True
    # Verify if the horizontal readings of the square are in words_alpha.txt
    for i in range(0, len(square), order):
        if horiz_word:
            horiz_word = EnglishDictionary.is_word(square[i:i + order])
            if not horiz_word:
                # Indicates one horizontal word is not in words_alpha.txt, meaning we have an invalid a crossword square
                return False
    # Same as horizontal verification but vertically
    for j in range(order):
        if verti_word:
            verti_word = EnglishDictionary.is_word(square[j:len(square):order])
            if not verti_word:
                return False
    # Indicates that all word(s) were in words_alpha.txt, meaning the word(s) forms a crossword square
    return True


def menu_check_crossword_square():
    user_square = get_crossword_square()
    crossword_square = check_crossword_square(user_square)
    # Calculate order to properly print each word in the crossword square
    square_root = 1/2
    order = int(len(user_square) ** square_root)
    if crossword_square:
        # Print all the originally inputted words
        for i in range(0, len(user_square), order):
            print(user_square[i:i + order])
        print("Is a crossword square!")
    else:
        # Print all the originally inputted words
        for j in range(0, len(user_square), order):
            print(user_square[j:j + order])
        print("Is not a crossword square.")


def main():
    user_choice = -1
    # Depending on what the user chooses in get_menu_choice(), call that function then re-loop until user quits.
    while user_choice != 3:
        print_menu()
        user_choice = get_menu_choice()
        print()
        if user_choice == 1:
            menu_check_palindrome()
            print()
        elif user_choice == 2:
            menu_check_crossword_square()
            print()
        elif user_choice == 3:
            print("Quitting...")


main()
