lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
decimal_numbers_list = '0123456789'

def caesar_cipher(text, letter_dislocator, number_dislocator):
    splitted_string = text.split() # split the string into a list of strings in order to work with spaces
    dict_lower = {} # creates a dictionary for lowercase letters in order to stabilish key-value pairs between them and the letters for the encrypted alphabet
    dict_upper = {} # creates a dictionary for uppercase letters in order to stabilish key-value pairs between them and the letters for the encrypted alphabet
    dict_numbers = {} # creates a dictionary for numbers in order to stabilish key-value pairs between them and the encrypted numbers
    for lower_index in range(len(lowercase_alphabet)): # for every letter in the alphabet
        if lower_index + letter_dislocator < 26: # checks if the letter won't return an index out of range error
            dict_lower[lowercase_alphabet[lower_index]] = lowercase_alphabet[lower_index + letter_dislocator] # creates an key-value pair of letter : letter in the encrypted alphabet
        else: # if (letter_index + n) surpasses the length of the alphabet
            dict_lower[lowercase_alphabet[lower_index]] = lowercase_alphabet[lower_index + letter_dislocator - 26] # the letter in the encrypted alphabet will be the (i + n - 26)th letter of the original alphabet
    for upper_index in range(len(uppercase_alphabet)): # this entire for loop does the same thing as the previous but for uppercase letters
        if upper_index + letter_dislocator < 26:
            dict_upper[uppercase_alphabet[upper_index]] = uppercase_alphabet[upper_index + letter_dislocator] 
        else: 
            dict_upper[uppercase_alphabet[upper_index]] = uppercase_alphabet[upper_index + letter_dislocator - 26]
    for number_index in range(len(decimal_numbers_list)):
        if number_index + number_dislocator < 10: # this loop does the same thing as the previous loops but for the numbers
            dict_numbers[decimal_numbers_list[number_index]] = decimal_numbers_list[number_index + number_dislocator] 
        else: 
            dict_numbers[decimal_numbers_list[number_index]] = decimal_numbers_list[number_index + number_dislocator - 10]
    finalstring = '' # creates an empty string that will be used on the output
    for set_of_characters in splitted_string: # analyze each word in the list of strings we've made with text.split()
        for character in set_of_characters: # analyze each character in the word we've got
            if character not in dict_lower and character not in dict_upper and character not in dict_numbers: # if it is not a number, or letter
                finalstring += character # the code won't encrypt the character and will just add it to the final message (it's not a problem at all)
            elif character.isdigit(): # if the character is a number
                finalstring += dict_numbers[character] # the code will add the encrypted number to the final message
            elif character.islower(): # if the character is a lowercase letter
                finalstring += dict_lower[character] # the code will add the encrypted lowercase letter to the final message
            elif character.isupper(): # if the character is a uppercase letter
                finalstring += dict_upper[character] # the code will add the encrypted uppercase letter to the final message
        finalstring += ' ' # adds a space when every set of characters is finished encrypting
    output = finalstring # the output receives the string contained in the variable finalstring
    print(f'Encrypted message: {output}') 
    return output
    
def descaesar_descipher(output, letter_dislocator, number_dislocator): # given the text and the dislocator numbers, we can uncrypt the message.
    # the code is the same as the caesar_cifer one, but with logical changes to turn possible the uncryptation of the message
    uncrypt_dict_lower = {}
    uncrypt_dict_upper = {}
    uncrypt_dict_numbers = {}
    for lower_index in range(len(lowercase_alphabet)):
        if lower_index - letter_dislocator < 0:
            uncrypt_dict_lower[lowercase_alphabet[lower_index]] = lowercase_alphabet[26 + (lower_index - letter_dislocator)]
        else:
            uncrypt_dict_lower[lowercase_alphabet[lower_index]] = lowercase_alphabet[lower_index - letter_dislocator]
    for upper_index in range(len(uppercase_alphabet)):
        if upper_index - letter_dislocator < 0:
            uncrypt_dict_upper[uppercase_alphabet[upper_index]] = uppercase_alphabet[26 + (upper_index - letter_dislocator)]
        else:
            uncrypt_dict_upper[uppercase_alphabet[upper_index]] = uppercase_alphabet[upper_index - letter_dislocator]
    for number_index in range(len(decimal_numbers_list)):
        if number_index - number_dislocator < 0:
            uncrypt_dict_numbers[decimal_numbers_list[number_index]] = decimal_numbers_list[10 + (number_index - number_dislocator)]
        else:
            uncrypt_dict_numbers[decimal_numbers_list[number_index]] = decimal_numbers_list[number_index - number_dislocator]
    splitted_output = output.split()
    uncrypted_text = ''
    for set_of_characters in splitted_output:
        for character in set_of_characters:
            if character not in uncrypt_dict_lower and character not in uncrypt_dict_upper and character not in uncrypt_dict_numbers:
                uncrypted_text += character
            elif character.isdigit():
                uncrypted_text += uncrypt_dict_numbers[character]
            elif character.islower():
                uncrypted_text += uncrypt_dict_lower[character]
            elif character.isupper():
                uncrypted_text += uncrypt_dict_upper[character]
        uncrypted_text += ' '
    uncrypted_message = uncrypted_text
    print(f'Uncrypted message: {uncrypted_message}')
    return uncrypted_message

message = input('Write here your message: ')
letter_dislocator = int(input('Input here the amount of letters you want to dislocate in the encrypted message: '))
number_dislocator = int(input('Input here the amount of numbers you want to dislocate in the encrypted message: '))
caesar_cipher(message, letter_dislocator, number_dislocator)

received_message = input("Write here the message you've received: ")
received_letter_dislocator = int(input("Write here the letter dislocator you've received: "))
received_number_dislocator = int(input("Write here the number dislocator you've received: "))
descaesar_descipher(received_message, received_letter_dislocator, received_number_dislocator)