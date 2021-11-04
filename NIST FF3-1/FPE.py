#%%
import math
#%%
radix = 12
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


           
def reverse_in_bytes(X):
    Y = X
    Y = list(Y)
    X = list(X)
    
    for i in range(0,len(X)):
        for j in range(1, 8):
            Y[(8*i)+j] = X[8*(len(X)-1-i)+j]
            
    return Y[1:8*len(X)]
    



# %%
for i in range(8):
    if i%2==0:
        m = u # u = 8
        W = T_r
    else:
        m = v # v = 8
        w = T_l



