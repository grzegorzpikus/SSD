import pyperclip
import math


def main():

    myKey = int(input('Provide security key: '))
    my_task = input('For encryption type e, for decryption type d: ')

    if my_task == 'e':
        myMessage = input('Put here your message: ')
        ciphertext = encryptMessage(myKey, myMessage)
        print('This was my message: \n'+myMessage)
        print('This is my encrypted message: \n'+ciphertext)
    elif my_task == 'd':
        ciphertext = input('Put here your encrypted message: ')
        plaintext = decryptMessage(myKey, ciphertext)
        print('This was my encrypted message: \n'+ciphertext)
        print('This is my message: \n' + plaintext)
    else:
        print('Wrong command, try again.')
        exit()

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext)  # Cipher text


def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (
                col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)


if __name__ == '__main__':
    main()