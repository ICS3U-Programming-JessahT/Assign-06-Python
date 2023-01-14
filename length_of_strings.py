#!/usr/bin/env python3

# Created By: Jessah
# Date: January 13, 2023
# This program ask the user for words and adds them to a list
# Then displays the length of each string in a list

# function to count the length of the list of strings
def count_strings(word, list_of_words):
    # empty list to add length of each word
    length = []
    for word in list_of_words:
        # append word to length with amount
        length.append(len(word))
    # return the length to main
    return length


def main():
    # initialize counter
    counter = 0
    # empty list to add user words in
    word_list = []
    # ask the user how they want to add to list
    amount = input("How many strings do want in the list?: ")
    # catch strings, negative and decimal numbers
    try:
        number = int(amount)
    except (Exception):
        print("{} is invalid, Try an integer".format(amount))
    else:
        if number <= 0:
            print("{} is invalid, Try a positive integer".format(number))
        else:
            for counter in range(number):
                # ask the user for a word
                user_words = input("Enter a word: ")
                print("{} was added to the list".format(user_words))
                # add the user word to list
                word_list.append(user_words)
                counter += counter
            # call function
            string_length = count_strings(user_words, word_list)
            print()
            # display the length of strings to user
            print("the length of each word is:")
            print(word_list)
            print(string_length)


if __name__ == "__main__":
    main()
