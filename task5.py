""" Salvatore La Paglia - 2023 Computer science NEA.  """



# Import standard modules.
import os



# Constants.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def get_mode() -> int:
    """ Asks the user whether they would like the file to be encrypted or decrypted. If the user
    writes `0` then they will be instructing the program to encrypt. And if they write `1`, they
    will be instructing the program to decrypt.
     
    Returns:
        user_input_mode: int -> An integer which represents the mode. `0` = encrypt, `1` = decrypt. 
    """

    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input_mode = input('Enter 0 to encrypt, 1 to decrypt: ')

        # Sanitizes the input but removing trailing whitespace.
        user_input_mode = user_input_mode.strip()

        # Checks whether the given input is a number and is between 1 and 0 inclusive. If not, 
        # prints an error message and continues the loop.
        if not (user_input_mode.isdigit()) or (not 0 <= int(user_input_mode) <= 1):
            print('Please only enter 0 for encryption and 1 for decryption!')
            continue

        # Changes the state of the validation process to successful.
        successful = True

    # Returns the mode.
    return int(user_input_mode)
    


def get_filename() -> str:
    """ Asks the user for a filename which points to the location of the file which will be either
    encrypted or decrypted. If the filename doesn't exist, is not a file, the filename points to 
    this program or the system doesn't have permission to read or write the file then the user is 
    asked again. If the given filename passes the tests, then the filename is returned to the 
    caller.
     
    Returns:
        user_input_filename: str -> A filename pointing to the desired filename.  """
    
    # Variable responsible for holding the state of the validation process.
    successful = False

    # Loops until the validation process is successful.
    while not successful:

        # Gets the users input.
        user_input_filename = input('Enter a valid filename: ')

        # Sanitizes the input but removing trailing whitespace and converting the path to be 
        # absolute.
        user_input_filename = os.path.abspath(user_input_filename.strip())

        # Checks whether the given input is a filename which exists. If not, an error message is
        # printed and the loop is continued.
        if not os.path.exists(user_input_filename):
            print('Please enter a valid filename!')
            continue

        # Checks whether the filename points to a file. If not, prints an error message and 
        # continues the loop.
        if not os.path.isfile(user_input_filename):
            print('Please enter a filename which points to a file!')
            continue

        # Checks whether the filename points to this program. If so, prints an error message and
        # continues the loop.
        if os.path.abspath(user_input_filename) == __file__:
            print('Please enter a filename which doesn\'t point to this program!')
            continue

        # Checks whether the user has READ and WRITE permissions to the pointed filename. If not, 
        # an error message is printed and the loop is continued.
        if (not os.access(user_input_filename, os.R_OK) or (not os.access(user_input_filename, os.W_OK))):
            print('Please enter a filename in which you have access to write and read!')
            continue
        
        # Changes the state of the validation process to successful.
        successful = True

    # Returns the filename.
    return user_input_filename
        



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
    """ Asks the user for a key, a filename and to indicate in some way whether the content of the
    file should be encrypted or decrypted. The file is then opened and if the instruction is to 
    encrypt it, the program reads the content of the file and encrypt it using a Caesar Cipher with
    the shift provided by a key. The encrypted content is then written to a file with the same name
    as the plain text with the word ENCRYPTED at the end. The reverse is true if the instruction is
    to decrypt the contents of a file, but the output file has the word DECRYPTED at the end.

    Returns: `None` -> Nothing to return. """

    # Gets the mode, filename and key.
    mode = get_mode()
    filename = get_filename()
    key = get_key()

    # Opens the file pointed by the filename in READ TEXT mode and reads the content.
    with open(filename, 'rt') as file:
        content = file.read()

    # Sets the mode type to ENCRYPTED if mode is 0 and to DECRYPTED if mode is 1. Reverses the key
    # shift if mode is 1.
    mode_type = 'ENCRYPTED'
    if mode == 1:
        key = -key
        mode_type = 'DECRYPTED'
    
    # Creates a variable which holds the new content characters.
    new_content = ''

    # Converts the file content to uppercase, then iterates through each character.
    for character in content.upper():

        # Checks whether the character is in the alphabet constant. 
        if character in ALPHABET:

            # Creates a ciphered index by getting the index of the character in the alphabet and 
            # then adding a shift via the key. This is then modulo divided so that the index 
            # doesn't exceed the length of the alphabet constant.
            ciphered_index = (ALPHABET.find(character) + key) % len(ALPHABET)

            # Gets the character using the ciphered index.
            character = ALPHABET[ciphered_index]

        # Adds the character to the new content variable.
        new_content += character

    # Gets the path, basename and extension.
    path, basename_complete = os.path.split(filename)
    basename, extension = os.path.splitext(basename_complete)

    # Starts the basename at 1.
    basename_count = 1

    # Creates a filename with the mode type added to the end (ENCRYPTED | DECRYPTED).
    new_filename = f"{path}{os.sep}{basename} {mode_type}{extension}"

    # Checks if the new filename exists.
    if os.path.exists(new_filename):

        # Variable responsible for holding the state of the validation process.
        successful = False

        # Loops until the validation process is successful.
        while not successful:

            # Creates a new basename with the added basename count and then a new filename.
            new_basename_complete = f"{basename} {mode_type} ({basename_count}){extension}"
            new_filename = f"{path}{os.sep}{new_basename_complete}"

            # Checks whether the new filename exists, if so, increments the basename count and 
            # continues the loop
            if os.path.exists(new_filename):
                basename_count += 1
                continue

            # Changes the state of the validation process to successful.
            successful = True

    # Opens the file pointed by the new filename in WRITE TEXT mode and writes the new content.
    with open(new_filename, 'wt') as file:
        file.write(new_content)


if __name__ == '__main__':
    main()