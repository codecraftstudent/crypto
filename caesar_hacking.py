#msg = 'GUVF VF ZL FRPERG ZRFFNTR.'
msg = 'PBQRPENSG YNO EBPXF!'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(ALPHABET)):

    # It is important to set result to the blank string so that the
    # previous iteration's value for result is cleared.
    result = ''

    # The rest of the program is the same as the original Caesar program:

    # run the encryption/decryption code on each symbol in the msg
    for symbol in msg:
        if symbol in ALPHABET:
            num = ALPHABET.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(ALPHABET)

            # add number's symbol at the end of result
            result = result + ALPHABET[num]

        else:
            # just add the symbol without encrypting/decrypting
            result = result + symbol

    # display the current key being tested, along with its decryption
    print('Key #%s: %s' % (key, result))
