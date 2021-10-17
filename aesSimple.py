from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode

key = b'123495678abcde5$'# 16 bytes which is 16*8 = 128
plain_text = b'4921947532202293' # 16 bytes
cipher = AES.new(key, AES.MODE_CTR)
cipher_text = cipher.encrypt(plain_text)
nonce = cipher.nonce

# Decryption
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)  # Setup cipher
original_data = cipher.decrypt(cipher_text)

print(cipher_text)
print(len(cipher_text))
print(cipher_text[0:8])
print(len(cipher_text[0:8]))
