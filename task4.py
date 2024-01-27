""" Salvatore La Paglia - 2023 Computer science NEA.  """



# Constants.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def get_message() -> str:
    """ Asks the user for their message which must be at least 20 characters long. The input is 
    validated, and if it does not meet the requirements, the user will be asked to try again. This
    is then converted to uppercase and returned to the caller.
     
    Returns:
        user_input_message: str -> The uppercase version of the user input. """

    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input_message = input('Enter a message which is at least 20 characters long: ')

        # Sanitizes the input but removing trailing whitespace.
        user_input_message = user_input_message.strip()

        # Checks whether the given input is fewer than 20 characters long. If so, prints out an
        # error message and continues the loop.
        if len(user_input_message) < 20:
            print('Please enter a message which is at least 20 characters long!')
            continue

        # Changes the state of the validation process to successful.
        successful = True

    # Returns the uppercase version of the user input to the caller.
    return user_input_message.upper()



def get_key() -> None:
    """ Asks the user for a key which should be an integer between 1 and 25 inclusive. he input is 
    validated, and if it does not meet the requirements, the user will be asked to try again. This 
    is then returned to the caller. 
    
    Returns:
        user_input_key: int -> The key (an integer between 1 and 25 inclusive). """
    
    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input_key = input('Enter a key which is an integer between 1 and 25 inclusive: ')

        # Sanitizes the input but removing trailing whitespace.
        user_input_key = user_input_key.strip()

        # Checks whether the given input is a digit string. If not, prints an error message and 
        # continues the loop.
        if not user_input_key.isdigit():
            print('Please only enter a number!')
            continue

        # Checks whether the given input is is an integer between 1 and 25 inclusive. If not, 
        # prints an error message and continues the loop.
        if not 1 <= int(user_input_key) <= 25:
            print('Please enter a number between 1 and 25 inclusive!')
            continue

        # Changes the state of the validation process to successful.
        successful = True

    # Returns the key.
    return int(user_input_key)



def main() -> None:
    """ Asks the user for their message which must be at least 20 characters long. This is then
    converted to uppercase. Then it asks the user for a key which should be an integer between 1 
    and 25 inclusive. Both inputs will be validated and if the user provides values that do not 
    meet these requirements, they will be asked to enter them again. The program should then 
    perform a Caesar Cipher on the message provided by the user, using a shift of the value 
    provided by the user. The ciphered message is then printed. 
    
    Returns: `None` -> Nothing to return. """

    # Gets the message and key.
    message = get_message()
    key = get_key()
        
    # Creates a variable which holds the ciphered characters.
    encrypted_message = ''

    # Iterates through every character in the given message.
    for character in message:

        # Checks whether the character is in the alphabet constant.
        if character in ALPHABET:

            # Creates a ciphered index by getting the index of the plaintext character in the 
            # alphabet and then adding a shift via the key. This is then modulo divided so that the
            # index doesn't exceed the length of the alphabet constant.
            ciphered_index = (ALPHABET.find(character) + key) % len(ALPHABET)

            # Gets the character using the ciphered index.
            character = ALPHABET[ciphered_index]

        # Adds the character to the encrypted message variable.
        encrypted_message += character

    # Prints the encrypted message.
    print(encrypted_message)



if __name__ == '__main__':
    main()