""" Salvatore La Paglia - 2023 Computer science NEA.  """



def main() -> None:
    """ Asks the user to enter a sentence that is at least 20 characters in length. If the input is
    less than 20 characters in length then the user will be asked to try again. It then counts the
    number of letters in this string and output an uppercase version of the string with the count 
    of letters. 
    
    Returns: `None` -> Nothing to return."""

    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input = input('Enter a sentence which is at least 25 characters long: ')

        # Sanitizes the input but removing trailing whitespace.
        user_input = user_input.strip()

        # Checks whether the given input is fewer than 20 characters long. If so, prints an error
        # message and continues the loop.
        if len(user_input) < 20:
            print('Please enter a sentence which is at least 25 characters long!')
            continue
        
        # Changes the state of the validation process to successful.
        successful = True
    
    # Prints the uppercase version and length of the given single letter input.
    print(f"{user_input.upper()} {len(user_input)}")



if __name__ == '__main__':
    main()