from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode

# AES Cipher class
class AEScipher:
    def __init__(self, key, plain_text):  
        self.key = key
        self.plain_text = plain_text
    def getKey(self, key):
        self.key = key
    def getPlainText(self, plain_text):
        self.plain_text = plain_text
    def encrypt(self):
        cipher = AES.new(self.key, AES.MODE_CTR)
        cipher_text = cipher.encrypt(self.plain_text)
        return cipher_text, cipher.nonce
    def decrypt(self, cipher_text, nonce):
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)  # Setup cipher
        original_data = cipher.decrypt(cipher_text)
        return original_data

# Byte wise xor

def byte_xor(ba1, ba2):
    """ XOR two byte strings """
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


key = b'123495678abcde5$'# 16 bytes which is 16*8 = 128
plain_text = b'4921947532202293' # 16 bytes


l0 = plain_text[0:8]
r0 = plain_text[9:16]
aes = AEScipher(key, r0)
f0,n0 = aes.encrypt()
r1 = byte_xor(f0,l0)
l1 = r0

# Format checking, return True if format is followed, and false if format is not followed

def format(cipher):
    for i in cipher:
        if i>=48 and i<=57:
            pass
        else:
            return False
    return True

 
print(format(b'1235'))
print(format(b'abcde%#'))
'''
cipher_text, nonce= aes.encrypt()
original_data = aes.decrypt(cipher_text, nonce)'''
