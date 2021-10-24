from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.Padding import pad, unpad

block = 16

# AEScipher class
class AEScipher:
    def __init__(self, key, plain_text):  
        self.key = key
        self.plain_text = plain_text
    def getKey(self, key):
        self.key = key
    def getPlainText(self, plain_text):
        self.plain_text = plain_text
    def encrypt(self):
        cipher = AES.new(self.key, AES.MODE_ECB)
        cipher_text = cipher.encrypt(pad(self.plain_text,block))
        return cipher_text 
    def decrypt(self, cipher_text):
        cipher = AES.new(self.key, AES.MODE_ECB)
          # Setup cipher
        original_data = cipher.decrypt(unpad(cipher_text,block))
        return original_data


# Function for bytewise XOR
def byte_xor(ba1, ba2):
    """ XOR two byte strings """
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

# Function for veryfing the format
def format(cipher):
    for i in cipher:
        if i>=48 and i<=57:
            pass
        else:
            return False
    return True

# global variables
key = b'123495678abcde5$'# 16 bytes which is 16*8 = 128
plain_text = b'4921947532202293' # 16 bytes

def feistel_forward(key_,plain_text_):
    l=[]
    r=[]
    aes = []
    l.append(plain_text_[0:8])
    r.append(plain_text_[8:16])

    for j in range(7):
        aes.append(AEScipher(key_,r[j]))
        tmp = aes[j].encrypt()
        r.append(byte_xor(tmp,l[j]))
        l.append(r[j])
    return l,r
l,r = feistel_forward(key,plain_text)        
#print("Left list :",l,"\n")
#print("Right List :",r, "\n")
#print(len(l))
#print(len(l+r))




c,d =feistel_forward(key,r[7]+l[7])

#print(c[7]+d[7])
c[7],d[7] = d[7],c[7]

print(c[7]+d[7])








'''
l0 = plain_text[0:8]
r0 = plain_text[9:16]
aes = AEScipher(key, r0)
f0,n0 = aes.encrypt()
r1 = byte_xor(f0,l0)
l1 = r0'''

'''
cipher_text, nonce= aes.encrypt()
original_data = aes.decrypt(cipher_text, nonce)'''

