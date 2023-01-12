# TODO
from cs50 import get_string


def main():

    # Get credit card number from user
    card = get_string("Number: ")
    length = len(card)

    # Declare variables
    array = []
    first_step = 0
    second_step = 0

    # if credit card number meets appropriate length, do the following:
    if length == 13 or length == 15 or length == 16:

        # Put credit card digits into an array
        for i in range(length):
            array.append(int(card[i]))

        # Perform first step of algorithm
        for j in range(length-2, -1, -2):

            if ((array[j] * 2) > 9):
                first_step += (((array[j] * 2) % 10) + 1)

            else:
                first_step += (array[j] * 2)

        # Perform second step of algorithm
        for k in range(length-1, -1, -2):
            second_step += array[k]

        # Perform third step of algorithm
        sum = first_step + second_step

        # Check if credit card passes validity test
        if ((sum % 10) == 0):

            # Check if card is American express
            if ((array[0] == 3) and ((array[1] == 4) or (array[1] == 7))):
                print("AMEX")

            # Check is card is VISA
            elif (array[0] == 4):
                print("VISA")

            # Check if card is MasterCard
            elif ((array[0] == 5) and ((array[1] > 0) and (array[1] < 6))):
                print("MASTERCARD")

            # If card is neither AMEX, VISA, or MASTERCARD, then return error message
            else:
                print("INVALID")
        else:
            print("INVALID")

    else:
        print("INVALID")


if __name__ == "__main__":
    main()