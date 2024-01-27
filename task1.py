""" Salvatore La Paglia - 2023 Computer science NEA.  """



def main() -> None:
    """ Asks the user for a single character input. Validates that the input is a single character 
    and that the character is a letter. If the input does not meet the requirements, then the 
    program asks the user to input again and repeat this until a valid input is received. Then 
    converts the input to uppercase. Displays on the screen the UPPER-CASE input and the ASCII 
    code for that character too. 
    
    Returns: `None` -> Nothing to return. """

    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input = input('Enter single letter input: ')

        # Sanitizes the input but removing trailing whitespace.
        user_input = user_input.strip()

        # Checks whether the length of given input is equal to 1 (single character). If not, prints
        # an error message and continues the loop.
        if len(user_input) != 1:
            print('Please enter a single character input!')
            continue

        # Checks whether the given input is an alphabetic string. If not, prints an error message
        # and continues the loop.
        if not user_input.isalpha():
            print('Please ensure that the character is a letter!')
            continue

        # Changes the state of the validation process to successful.
        successful = True

    # Prints the uppercase version and ASCII code for the given single letter input.
    print(f"{user_input.upper()} {ord(user_input)}")



if __name__ == '__main__':
    main()