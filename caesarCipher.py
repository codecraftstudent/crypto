# the string to be encrypted/decrypted
msg = 'Codecraft Lab rocks!'

# the encryption/decryption key
key = 13

# tells the program to encrypt or decrypt
mode = 'encrypt' # set to 'encrypt' or 'decrypt'

# every possible symbol that can be encrypted
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the msg
result = ''

# capitalize the string in msg
msg = msg.upper()

# run the encryption/decryption code on each symbol in the msg string
for symbol in msg:
    if symbol in ALPHABET:
        # get the encrypted (or decrypted) number for this symbol
        num = ALPHABET.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # ALPHABET or less than 0
        if num >= len(ALPHABET):
            num = num - len(ALPHABET)
        elif num < 0:
            num = num + len(ALPHABET)

        # add encrypted/decrypted number's symbol at the end of result
        result = result + ALPHABET[num]

    else:
        # just add the symbol without encrypting/decrypting
        result = result + symbol

# print the encrypted/decrypted string to the screen
print(result)
