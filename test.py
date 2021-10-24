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
plain_text = b'492a947532202293' # 16 bytes

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

count = 0
x=10
while(x):
    l,r = feistel_forward(key,l[7]+r[7])        
    count = count+1
    x= x-1

print(count)
print(l[7]+r[7])

    
    


