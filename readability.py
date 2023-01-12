# TODO
from cs50 import get_string


def main():

    # Declare variables
    letter_count = 0.0
    word_count = 1.0
    sentence_count = 0.0

    # Prompt user for text
    text = get_string("Text: ")

    # Count characters
    length = len(text)

    # Count letters
    for i in range(length):

        if text[i].isalpha():
            letter_count += 1

        elif (text[i] == ' '):
            word_count += 1

        elif ((text[i] == '.') or (text[i] == '!') or (text[i] == '?')):
            sentence_count += 1

    # Calculate the average number of letters per 100 words in the text
    L = (letter_count / word_count) * 100

    # Calculate the average number of sentences per 100 words in the text
    S = (sentence_count / word_count) * 100

    # Calculate grade
    index = (0.0588 * L) - (0.296 * S) - 15.8
    index1 = round(index)

    # Display grade
    if index >= 16:
        print("Grade 16+")

    elif index < 1:
        print("Before Grade 1")

    else:
        print("Grade " + str(index1))


if __name__ == "__main__":
    main()