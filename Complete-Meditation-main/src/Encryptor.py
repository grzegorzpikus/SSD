from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class Encryptor:

    def __init__(self, newPassword, textToEncrypt):

        self.cipher = None
        self.ciphered_data = None
        self.PBKDF2Key = None
        self.generateSalt()

        self.password = newPassword
        self.debugPlainText = textToEncrypt

        if not (self.password or textToEncrypt):
            print("must have password and something to encrypt")
        else:
            self.generatePBKDF2Key()
            self.textToEncryptInBytes = bytes(textToEncrypt, 'utf-8')

    def generateSalt(self):
        # this should be more random. Not NIST approved
        salt = get_random_bytes(32)
        self.salt = salt

    # generate key PBKDF2 key. Internal hashing
    # PBKDF2 minimise brute force attacks
    # PBKDF2 recommended if FIPS 140 compliance is required, which CERN requires
    # https: // cheatsheetseries.owasp.org / cheatsheets / Password_Storage_Cheat_Sheet.html
    def generatePBKDF2Key(self):
        self.PBKDF2Key = PBKDF2(self.password, self.salt, count=7000100, dkLen=32)
        with open('key.bin', 'wb') as keyToFile:
            keyToFile.write(self.PBKDF2Key)

    def cipherText(self):
        # cipher data
        self.cipher = AES.new(self.PBKDF2Key, AES.MODE_CBC)
        # the ciphered data is encrypted
        self.ciphered_data = self.cipher.encrypt(pad(self.textToEncryptInBytes, AES.block_size))
        return self.ciphered_data

    def writeCipheredDataToFile(self):
        # writing encrypted data to .bin file
        with open('encrypted.bin', 'wb') as cipheredWrite:
            cipheredWrite.write(self.cipher.iv)
            cipheredWrite.write(self.ciphered_data)

    def readCipheredDataFromFile(self):
        # reading encrypted data from .bin file
        with open('encrypted.bin', 'rb') as cipheredRead:
            ivFromFile = cipheredRead.read(16)
            dataToDecrypt = cipheredRead.read()

        self.cipher = AES.new(self.PBKDF2Key, AES.MODE_CBC, iv=ivFromFile)
        originalText = unpad(self.cipher.decrypt(dataToDecrypt), AES.block_size)
        return originalText


# # this is just to test the instansiation, uncomment to test it
# obj = Encryptor("bona-chips/&telephone", "Jag heter Maja")
# newVar = obj.salt
# print(newVar)
# print(obj.PBKDF2Key)
#
# obj.cipherText()
# obj.writeCipheredDataToFile()
# obj.readCipheredDataFromFile()
# print(obj.ciphered_data)




















