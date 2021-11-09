#%%
import math
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from test import reverseBytes

block = 16
#%%
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
#%%
radix = 10
minlen = 6
maxlen = 56
T = "ABD212A5D4C842"  # tweak string of length 56 (14 pairs of hexadecimal)
n = 16 # length of ciphertext
X = "5621875652796140"  # plaintext

u = math.ceil(n/2) # u = 8
v = n-u
A = X[0:8] # first 8 digits of plaintext(x)
B = X[8:16]


# %%

T_l = T[0:8]
T_r = T[8:16] + T[7] + str(0)  

#%%

# Functions

def num_radix(X):
    x = 0
    for i in range(1,len(X)):# length of plaintext = 16
        x = x*radix + int(X[i])
    return x

def string_radix(x,m): # v=8
    #m = len(x)
    X = list(x)
    x = int(x)
    for i in range(1,m+1):
        X[m+1-i] = x % radix
        x = math.floor(x/radix) # floor value
    k = ""
    for i in range(m):    
        k = k + str(X[i])
    return k # returns the plaintext
  

def num(X):
    x = 0
    for i in range(0,len(X)):
        x = 2*x + int(X[i])
    return x

          
def reverse(X):
    Y=X
    Y=list(Y)
    X=list(X)
    k = ""
    for i in range(0,len(X)):
        Y[i] = X[len(X)-1-i]
        k = k + Y[i]
    return k

def reverse_bytes(X):
    bytes_size = math.ceil(len(X)/8)
    r = [[] for i in range(bytes_size)]    
    count = 0
    for i in range(len(X)):
        if i % 8 == 0 and i != 0:
            count = count + 1        
        r[count].append(X[i])
    a = ""
    for i in range(len(r)):
        for j in range(8):
            a = a + r[len(r)-1-i][j]
    return a

def xor(a, b):
    y = int(a,2) ^ int(b,2)
    return '{0:b}'.format(y)

# %%
for i in range(8):
    if i%2==0:
        m = u # u = 8
        W = T_r
    else:
        m = v # v = 8
        W = T_l
    # converting hex to bin
    P = xor(bin(int(W,16))[2:], ('{:032b}'.format(i))) + '{:0192b}'.format(int(str(num_radix(reverse('{:096b}'.format(int(B))))),2))    

        

