#!/usr/bin/env python
# visit http://tool.lu/pyc/ for more information
import base64

# 加密前和加密后的len长度相同
flag = 'lhx'
def encode():
    ciphertext = []
    for i in range(len(flag)):
        if i % 2 == 0:
            s = ord(chr(i ^ ord(flag[i]))) + 10
        else:
            s = ord(chr(i ^ ord(flag[i]))) - 10
        ciphertext.append(str(s))
    
    return ciphertext[::-1]

# print(len(encode()))
# print(len(flag))
print(encode())