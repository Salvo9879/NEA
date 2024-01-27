""" Salvatore La Paglia - 2023 Computer science NEA.  """



def main() -> None:
    """ Asks the user for a numerical input. Validates that the input is a number in the range 1 to
    25 inclusive. If the input does not meet the requirements, then the program asks the user to 
    input again and repeats this until a valid input is received. Then preforms a modulo 2 division
    on the input value and then outputs the original input value and the result of the modulo 
    division. 
    
    Returns: `None` -> Nothing to return."""

    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input = input('Enter a number between 1 and 25 inclusive: ')

        # Sanitizes the input but removing trailing whitespace.
        user_input = user_input.strip()

        # Checks whether the given input is a digit string. If not, prints an error message and 
        # continues the loop.
        if not user_input.isdigit():
            print('Please only enter a number!')
            continue

        # Checks whether the given input is is an integer between 1 and 25 inclusive. If not, 
        # prints an error message and continues the loop.
        if not 1 <= int(user_input) <= 25:
            print('Please enter a number between 1 and 25 inclusive!')
            continue

        # Changes the state of the validation process to successful.
        successful = True

    # Prints the standard and modulo 2 division of the numerical input.
    print(f"{user_input} {int(user_input)%2}")


if __name__ == '__main__':
    main()